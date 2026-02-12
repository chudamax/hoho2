#!/usr/bin/env python3
# repo_brief_alltext.py
# Generate a Markdown dossier for a repo and EMBED contents of almost all text files.
# Defaults:
#   - Includes tracked + untracked files (if in a Git repo)
#   - Excludes ONLY .env files (e.g., .env, .env.*, **/.env, **/.env.*)
#   - Directory tree depth = 10
# No external dependencies. Python 3.8+.

import os, sys, re, json, argparse, subprocess
from pathlib import Path
from collections import Counter
from datetime import datetime

# ------------------ Logging ------------------

def log(msg, enabled):
    if enabled:
        print(msg, flush=True)

# ------------------ Git helpers ------------------

def run(cmd, cwd=None):
    try:
        out = subprocess.check_output(cmd, cwd=cwd, stderr=subprocess.DEVNULL)
        return out.decode("utf-8", "replace").strip()
    except Exception:
        return ""

def in_git_repo(root: Path) -> bool:
    return bool(run(["git", "rev-parse", "--is-inside-work-tree"], cwd=root))

def list_files_git(root: Path, include_untracked=True):
    tracked = run(["git", "ls-files", "-z"], cwd=root)
    files = [Path(p) for p in tracked.split("\x00") if p]
    if include_untracked:
        extra = run(["git", "ls-files", "--others", "--exclude-standard", "-z"], cwd=root)
        files += [Path(p) for p in extra.split("\x00") if p]
    return files

# ------------------ Filters ------------------

DEFAULT_IGNORES = {
    ".git",".hg",".svn",".DS_Store","__pycache__",".mypy_cache",".pytest_cache",".cache",
    ".idea",".vscode","node_modules","dist","build","out",".next",".nuxt",".parcel-cache",
    "target","bin","obj",".venv","venv","env",".tox",".coverage","coverage",".terraform",
    ".gradle",".serverless",".docusaurus","migrations","repo_brief","sensors/egress_proxy/packages",
    "sensors/egress_proxy/packages","sensors/falco/packages","sensors/fsmon/packages",
    "sensors/http_proxy/packages","sensors/pcap/packages"
}

BINARY_EXTS = {
    ".png",".jpg",".jpeg",".gif",".webp",".ico",".svgz",
    ".pdf",".zip",".gz",".bz2",".xz",".7z",".rar",
    ".mp3",".ogg",".mp4",".mov",".avi",".webm",
    ".woff",".woff2",".ttf",".eot",".icns"
}

# explicit .env exclusion only
ENV_PATH_REGEX = re.compile(r"(?i)(^|/)\.env($|[.\-/])")

# secret-ish line redaction
SUSPECT_LINE_REGEX = re.compile(
    r"(?i)\b(password|passwd|secret|token|api[_-]?key|authorization|bearer|private\s+key|BEGIN\s+RSA\s+PRIVATE\s+KEY)\b"
)

# ------------------ Content utils ------------------

def is_probably_binary(path: Path, sample_bytes=4096):
    try:
        with path.open("rb") as f:
            chunk = f.read(sample_bytes)
        if b"\x00" in chunk:
            return True
        nontext = sum(b < 9 or (13 < b < 32) for b in chunk)
        return (len(chunk) > 0 and nontext / len(chunk) > 0.30)
    except Exception:
        return True

def count_lines(path: Path, max_bytes=1_000_000):
    try:
        if path.stat().st_size > max_bytes:
            return 0
        with path.open("rb") as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

def redact_lines(text: str, enabled=True) -> str:
    if not enabled:
        return text
    out = []
    for line in text.splitlines():
        if SUSPECT_LINE_REGEX.search(line):
            if "=" in line:
                k, _, _v = line.partition("=")
                out.append(f"{k}=[REDACTED]")
            elif ":" in line:
                k, _, _v = line.partition(":")
                out.append(f"{k}: [REDACTED]")
            else:
                out.append("[REDACTED]")
        else:
            out.append(line)
    return "\n".join(out)

# ------------------ Language → code fence ------------------

LANG_BY_EXT = {
    ".py":"python",".ipynb":"", ".js":"javascript",".mjs":"javascript",".cjs":"javascript",
    ".ts":"ts",".tsx":"tsx",".jsx":"jsx",".rb":"ruby",".go":"go",".rs":"rust",".java":"java",
    ".kt":"kotlin",".kts":"kotlin",".cs":"csharp",".php":"php",".swift":"swift",".c":"c",
    ".h":"c", ".hpp":"cpp",".hh":"cpp",".hxx":"cpp",".cc":"cpp",".cpp":"cpp",".cxx":"cpp",
    ".scala":"scala",".pl":"perl",".sh":"bash",".bash":"bash",".zsh":"bash",".ps1":"powershell",
    ".sql":"sql",".r":"r",".jl":"julia",".dart":"dart",".lua":"lua",".yaml":"yaml",".yml":"yaml",
    ".json":"json",".toml":"toml",".md":"md",".rst":"", ".tex":"", ".html":"html",".css":"css",
    ".scss":"scss",".less":"less",".vue":"vue",".svelte":"svelte",".gradle":"", ".env":""
}

def fence_for(path: Path) -> str:
    return LANG_BY_EXT.get(path.suffix.lower(), "")

# ------------------ Repo info ------------------

def get_repo_info(root: Path):
    info = {}
    if in_git_repo(root):
        info["branch"] = run(["git","rev-parse","--abbrev-ref","HEAD"], cwd=root)
        info["commit"] = run(["git","rev-parse","--short","HEAD"], cwd=root)
        info["commit_date"] = run(["git","show","-s","--format=%ad","--date=iso"], cwd=root)
        info["commits"] = run(["git","rev-list","--count","HEAD"], cwd=root)
        log10 = run(["git","log","-n","10","--pretty=format:%h | %ad | %s","--date=short"], cwd=root)
        info["recent"] = log10.splitlines() if log10 else []
    return info

def lang_counts_and_loc(root: Path, files):
    histogram = Counter()
    loc = Counter()
    for rel in files:
        ext = Path(rel).suffix.lower()
        lang = LANG_BY_EXT.get(ext, "other") or "other"
        histogram[lang] += 1
        loc[lang] += count_lines(root/rel)
    return histogram, loc

# ------------------ File discovery ------------------

def gather_files(root: Path, include_untracked: bool, verbose: bool):
    if in_git_repo(root):
        files = list_files_git(root, include_untracked=include_untracked)
    else:
        files = []
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in DEFAULT_IGNORES and not d.startswith(".git")]
            for fn in filenames:
                rel = Path(dirpath) / fn
                rel = rel.relative_to(root)
                if any(seg in DEFAULT_IGNORES for seg in rel.parts):
                    continue
                files.append(rel)

    # 🔧 Apply ignores for BOTH paths (Git and non-Git)
    files = [p for p in files if not any(seg in DEFAULT_IGNORES for seg in Path(p).parts)]

    # existing binary-ext pruning
    files = [p for p in files if Path(p).suffix.lower() not in BINARY_EXTS]
    log(f"Discovered {len(files)} candidate files (pre-binary/text checks).", verbose)
    return files

def build_tree(root: Path, files, max_depth=10, max_entries=800):
    files = sorted([Path(f) for f in files], key=lambda p: (len(p.parts), str(p)))
    pruned = [f for f in files if len(f.parts) <= max_depth][:max_entries]
    out=[]
    def indent(n): return "  " * (n-1) + ("- " if n>0 else "")
    for p in pruned:
        parts = p.parts
        for i in range(1, min(len(parts), max_depth)+1):
            out.append(indent(i) + parts[i-1])
    seen=set(); ordered=[]
    for line in out:
        if line not in seen:
            seen.add(line); ordered.append(line)
    return "\n".join(ordered)

# ------------------ Markdown assembly ------------------

def build_markdown(
    root: Path,
    files,
    tree_depth: int,
    max_files: int,
    max_lines_per_file: int,
    max_bytes_per_file: int,
    max_total_bytes: int,
    redact: bool,
    verbose: bool
):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    repo_name = root.resolve().name
    info = get_repo_info(root)

    # Filter to text files, exclude .env* by path
    text_files = []
    for rel in files:
        p = root / rel
        ps = rel.as_posix()
        if ENV_PATH_REGEX.search(ps):
            continue
        if p.is_dir():
            continue
        if is_probably_binary(p):
            continue
        text_files.append(rel)

    text_files = sorted(set(text_files), key=lambda x: x.as_posix())
    log(f"Text-like files after filters (excluding .env*): {len(text_files)}", verbose)

    # language stats
    lang_hist, loc_hist = lang_counts_and_loc(root, text_files)

    # Start building MD
    lines=[]
    lines.append(f"# Repository Brief: {repo_name}\n")
    lines.append(f"_Generated {now}_\n")
    lines.append("## Quick Facts")
    if info:
        lines.append(f"- **Branch:** {info.get('branch','')}")
        lines.append(f"- **Commit:** {info.get('commit','')} ({info.get('commit_date','')})")
        lines.append(f"- **Total commits:** {info.get('commits','')}")
    lines.append(f"- **Files scanned:** {len(files)}")
    lines.append(f"- **Text files embedded (after filters):** {len(text_files)}\n")

    lines.append("## Language & LOC Overview (approx.)")
    total_files = sum(lang_hist.values()) or 1
    for lang, cnt in lang_hist.most_common():
        pct = cnt / total_files * 100.0
        loc = loc_hist.get(lang, 0)
        lines.append(f"- **{lang}** — files: {cnt} ({pct:.1f}%), LOC: {loc}")
    lines.append("")

    # Directory tree
    tree = build_tree(root, text_files, max_depth=tree_depth)
    lines.append(f"## Directory Tree (depth ≤ {tree_depth})\n")
    lines.append("```text")
    lines.append(tree or "(no files)")
    lines.append("```\n")

    # Recent commits
    if info.get("recent"):
        lines.append("## Recent Commits")
        lines += [f"- {l}" for l in info["recent"]]
        lines.append("")

    # Embedded contents
    lines.append("## Files (embedded, trimmed)")
    lines.append("> Secret-looking lines are redacted by default. Large files are truncated to stay within budgets.\n")

    total_bytes = 0
    embedded = 0

    for rel in text_files:
        if embedded >= max_files:
            lines.append(f"<!-- stopped after reaching --max-files ({max_files}) -->")
            break
        full = root / rel
        try:
            raw = full.read_bytes()
        except Exception:
            continue

        # per-file cap
        snippet = raw if len(raw) <= max_bytes_per_file else raw[:max_bytes_per_file]
        text = snippet.decode("utf-8", errors="replace")
        lines_list = text.splitlines()
        truncated = False
        if len(lines_list) > max_lines_per_file:
            lines_list = lines_list[:max_lines_per_file]
            truncated = True
        text = "\n".join(lines_list)
        text = redact_lines(text, enabled=redact)

        fence = fence_for(rel)
        size_kb = len(raw) / 1024.0
        lines.append(f"### `{rel}`  _(~{size_kb:.1f} KB; showing ≤{max_lines_per_file} lines)_")
        lines.append(f"```{fence}".rstrip())
        lines.append(text)
        lines.append("```")
        if truncated or len(raw) > len(snippet):
            lines.append("<!-- trimmed: file exceeded per-file limits -->")
        lines.append("")

        embedded += 1
        total_bytes += len(snippet)
        if total_bytes >= max_total_bytes:
            lines.append(f"<!-- stopped after reaching --max-total-bytes ({max_total_bytes} bytes) -->")
            break

    return "\n".join(lines)

# ------------------ Main ------------------

def main():
    ap = argparse.ArgumentParser(
        description="Generate a Markdown brief for a repo and EMBED contents of nearly all text files (excluding .env*)."
    )
    ap.add_argument("--repo", default=".", help="Path to repo root (default: .)")
    ap.add_argument("--out", default="REPO_BRIEF.md", help="Output Markdown file (ignored if --stdout)")
    ap.add_argument("--stdout", action="store_true", help="Print Markdown to STDOUT instead of writing a file")
    ap.add_argument("--tree-depth", type=int, default=10, help="Directory tree depth (default: 10)")
    # default: include untracked
    ap.add_argument("--tracked-only", action="store_true",
                    help="Only include files tracked by Git (default: include untracked too if in a Git repo)")
    ap.add_argument("--verbose", "-v", action="store_true", help="Verbose logs")
    ap.add_argument("--no-redact", action="store_true", help="Disable redaction of secret-looking lines")

    # Budgets (defaults generous)
    ap.add_argument("--max-files", type=int, default=3000, help="Max number of files to embed (default: 3000)")
    ap.add_argument("--max-lines-per-file", type=int, default=800, help="Max lines per file (default: 800)")
    ap.add_argument("--max-bytes-per-file", type=int, default=350_000, help="Max bytes per file before trimming (default: 350k)")
    ap.add_argument("--max-total-bytes", type=int, default=8_000_000, help="Total bytes budget across all embedded files (default: 8MB)")

    args = ap.parse_args()

    root = Path(args.repo).resolve()
    if not root.exists():
        print(f"ERROR: repo path does not exist: {root}", file=sys.stderr)
        sys.exit(2)

    include_untracked = not args.tracked_only

    log(f"Scanning repository at: {root}", args.verbose)
    files = gather_files(root, include_untracked=include_untracked, verbose=args.verbose)

    md = build_markdown(
        root=root,
        files=files,
        tree_depth=args.tree_depth,
        max_files=args.max_files,
        max_lines_per_file=args.max_lines_per_file,
        max_bytes_per_file=args.max_bytes_per_file,
        max_total_bytes=args.max_total_bytes,
        redact=not args.no_redact,
        verbose=args.verbose
    )

    if args.stdout:
        print(md)
        log("Printed Markdown to STDOUT.", args.verbose)
    else:
        out_path = Path(args.out).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")
        print(f"Wrote {out_path}", flush=True)

if __name__ == "__main__":
    main()
