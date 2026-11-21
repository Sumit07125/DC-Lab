# Experiment No. 10
# WAP to Implement Group Communication
# Client Program

import socket
import threading

HOST = "127.0.0.1"  # Use the server computer's IP for another computer.
PORT = 12345


def receive_messages(client_socket):
    """Receive and display messages broadcast by the server."""
    try:
        with client_socket.makefile("r", encoding="utf-8") as reader:
            for message in reader:
                print("\n" + message.rstrip())
    except (ConnectionError, OSError):
        pass


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
    except OSError:
        print("Could not connect. Make sure the server is running.")
        client_socket.close()
        return

    print("Connected to the group communication server.")
    print("Type a message to send it to the other clients.")
    print("Type 'exit' to disconnect.\n")

    receiver = threading.Thread(
        target=receive_messages,
        args=(client_socket,),
        daemon=True
    )
    receiver.start()

    try:
        while True:
            message = input("Enter message: ").strip()

            if message.lower() == "exit":
                break

            if message:
                client_socket.sendall((message + "\n").encode("utf-8"))

    except (EOFError, KeyboardInterrupt):
        print("\nDisconnecting...")
    except (ConnectionError, OSError):
        print("Connection to the server was lost.")
    finally:
        try:
            client_socket.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        client_socket.close()
        print("Client disconnected.")


if __name__ == "__main__":
    main()
