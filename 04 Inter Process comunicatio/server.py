# Experiment No. 4: Inter-Process Communication (Server Program)
import socket

HOST = "127.0.0.1"  # localhost
PORT = 6666


def start_server() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Server listening on {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected to client: {addr}")
            data = conn.recv(1024).decode("utf-8").strip()
            if data:
                a, b = map(int, data.split(","))
                print(f"Received: {a}, {b}")
                print(f"Sum = {a + b}")


if __name__ == "__main__":
    try:
        start_server()
    except Exception as err:
        print(f"Server error: {err}")