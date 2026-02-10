import socket
import threading


def run_tcp_banner(host: str, port: int, banner: str) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    def loop():
        while True:
            conn, _ = sock.accept()
            conn.sendall(banner.encode())
            conn.close()

    threading.Thread(target=loop, daemon=True).start()
