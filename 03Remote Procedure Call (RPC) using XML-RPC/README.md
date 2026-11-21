# Practical No. 3 – XML-RPC (Remote Procedure Call)

## Aim

To implement remote procedure calls using XML-RPC in Python. A client invokes arithmetic functions on a server, and the server returns the results.

## Files in this folder

| File | Description |
|---|---|
| `server.py` | Creates the XML-RPC server and provides addition, subtraction, multiplication, and division functions. |
| `client.py` | Connects to the server and calls the remote arithmetic functions. |
| `README.md` | Instructions for setup, execution, and testing. |

## Requirements and dependencies

- Python 3 (Python 3.8 or later recommended).
- No third-party libraries are required.
- `xmlrpc.server` and `xmlrpc.client` are part of Python's standard library.
- Both programs in this example run on the same computer and communicate through `127.0.0.1` on port `8000`.

Check that Python is installed:

```bash
python --version
```

On some systems, use `python3 --version` instead.

### Installation

There is no package installation step. Do **not** run `pip install` for this practical.

## How to run the practical

### Step 1: Open the project folder

Open the `practical_3_xmlrpc` folder in VS Code or open a terminal in that folder. Make sure `server.py` and `client.py` are in the same folder.

### Step 2: Start the server

Open **Terminal 1** and run:

```bash
python server.py
```

The server starts listening at `http://127.0.0.1:8000/` and waits for client requests. Keep this terminal running.

### Step 3: Run the client

Open **Terminal 2** in the same project folder and run:

```bash
python client.py
```

The client connects to the server and remotely calls the four arithmetic functions. It also checks the division-by-zero condition.

### Step 4: Stop the server

Return to Terminal 1 and press **Ctrl+C**.

> If the `python` command is not recognized, try `python3 server.py` and `python3 client.py` (or `py server.py` and `py client.py` on Windows).

## Change the input numbers

In `client.py`, edit these two lines to test different values:

```python
a = 10
b = 5
```

Run the client again while the server is running.

## How the program works

1. The server defines the arithmetic functions: `add()`, `subtract()`, `multiply()`, and `divide()`.
2. `SimpleXMLRPCServer` starts an XML-RPC server on `127.0.0.1:8000`.
3. `register_function()` makes each function available to remote clients.
4. The client creates an `xmlrpc.client.ServerProxy` using the server URL.
5. Calls such as `server.add(a, b)` are sent to the server using XML-RPC.
6. The server executes the requested function and sends the result back to the client.
7. The `divide()` function handles a zero denominator and returns `Cannot divide by zero` instead of attempting the division.

## Troubleshooting

- **Connection refused / could not connect:** Start `server.py` first and leave it running.
- **Address already in use:** Another program may already be using port `8000`. Stop that program before running this server.
- **Different computers:** This example is configured for two programs on the same computer. For a multi-computer setup, the server must bind to a reachable network interface and the client must use the server computer's LAN IP address; firewall rules may also need to permit TCP port `8000`.

## Scope and note

This is a basic XML-RPC demonstration of remote procedure calls for arithmetic operations. It uses Python's built-in XML-RPC support and does not require an external package. The uploaded ZIP supplied for review contained the two Python source files only; it did not contain the written practical handout or its expected-output pages. Therefore, this README and code review are based on the implementation supplied in that ZIP.
