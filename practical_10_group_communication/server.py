# Experiment No. 10
# WAP to Implement Group Communication
# Server Program

import socket
import threading

HOST = "0.0.0.0"
PORT = 12345

clients = []
clients_lock = threading.Lock()


def broadcast(message, sender):
    """Send a message to every connected client except the sender."""
    data = (message + "\n").encode("utf-8")

    with clients_lock:
        for client in clients[:]:
            if client != sender:
                try:
                    client.sendall(data)
                except OSError:
                    clients.remove(client)
                    client.close()


def handle_client(client_socket, address):
    print("Client", address, "connected.")

    try:
        # Read complete messages, one line at a time.
        with client_socket.makefile("r", encoding="utf-8") as reader:
            for line in reader:
                message = line.strip()

                if message:
                    print("Received:", message)
                    broadcast(
                        "Client " + str(address[1]) + ": " + message,
                        client_socket
                    )

    except (ConnectionError, OSError):
        pass

    finally:
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)

        client_socket.close()
        print("Client", address, "disconnected.")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print("Server started. Waiting for clients...")

    try:
        while True:
            client_socket, address = server.accept()

            with clients_lock:
                clients.append(client_socket)

            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address),
                daemon=True
            )
            thread.start()

    except KeyboardInterrupt:
        print("\nServer is shutting down.")

    finally:
        with clients_lock:
            connected_clients = clients[:]
            clients.clear()

        for client in connected_clients:
            client.close()

        server.close()


if __name__ == "__main__":
    main()
