from hoho_core.dsl.matchers import match_rule
from hoho_core.dsl.actions import run_action


def evaluate_rules(behaviors: list[dict], req: dict, store, event: dict) -> dict:
    state = {
        "classification": event["classification"],
        "decision": event["decision"],
        "artifacts": event["artifacts"],
        "respond": None,
    }
    for rule in behaviors:
        if match_rule(rule, req):
            for action in rule.get("actions", []):
                run_action(action, state, req, store)
            if rule.get("respond"):
                state["respond"] = rule["respond"]
            break
    return state
