# Practical No. 3
# XML-RPC Client: Calls remote arithmetic operations

import xmlrpc.client

SERVER_URL = "http://127.0.0.1:8000/"


def main():
    # Values sent to the server for remote calculation.
    a = 10
    b = 5

    try:
        with xmlrpc.client.ServerProxy(SERVER_URL, allow_none=True) as server:
            print("Connected to XML-RPC server")
            print("Numbers:", a, "and", b)
            print("Addition:", server.add(a, b))
            print("Subtraction:", server.subtract(a, b))
            print("Multiplication:", server.multiply(a, b))
            print("Division:", server.divide(a, b))

            # Check the division-by-zero condition.
            print("Division by zero:", server.divide(a, 0))

    except (OSError, xmlrpc.client.Error) as error:
        print("Could not communicate with the server:", error)
        print("Make sure server.py is running before starting client.py.")


if __name__ == "__main__":
    main()
