# Practical No. 3
# XML-RPC Server: Remote Arithmetic Operations

from xmlrpc.server import SimpleXMLRPCServer


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Divide the first number by the second number."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def main():
    # Create the XML-RPC server on the local computer.
    with SimpleXMLRPCServer(
        ("127.0.0.1", 8000),
        allow_none=True,
        logRequests=False
    ) as server:
        # Make the arithmetic functions available to clients.
        server.register_function(add, "add")
        server.register_function(subtract, "subtract")
        server.register_function(multiply, "multiply")
        server.register_function(divide, "divide")

        print("XML-RPC server is running at http://127.0.0.1:8000/")
        print("Waiting for client requests... Press Ctrl+C to stop.")

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()
