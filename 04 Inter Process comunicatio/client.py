# Experiment No. 4: Inter-Process Communication (Client Program)
import socket

HOST = "127.0.0.1"  # localhost
PORT = 6666


def start_client() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        a = int(input("Enter 1st no:\n"))
        b = int(input("Enter 2nd no:\n"))

        client_socket.sendall(f"{a},{b}".encode("utf-8"))
        print("Numbers sent to server.")


if __name__ == "__main__":
    try:
        start_client()
    except ConnectionRefusedError:
        print("Connection failed: Start server.py first.")
    except ValueError:
        print("Invalid input: Enter integer numbers only.")
    except Exception as err:
        print(f"Client error: {err}")