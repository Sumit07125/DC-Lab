# Experiment No. 4: Inter-Process Communication

## Aim

To demonstrate inter-process communication between a client and a server using Python socket programming.

## Description

The server listens on **localhost (`127.0.0.1`)** at port **`6666`**. The client connects to the server, accepts two integers from the user, and sends them to the server as a comma-separated string. The server receives the values, converts them to integers, calculates their sum, and displays the result.

## Files

| File | Purpose |
|---|---|
| `server.py` | Starts the server and calculates the sum |
| `client.py` | Accepts user input and sends it to the server |

## Prerequisites

- Python 3 installed
- Both programs executed on the same computer
- Port `6666` available

## How to Run

Open the project folder in a terminal.

### 1. Start the Server

Open **Terminal 1** and run:

```bash
python server.py
```

Expected server output:

```text
Server listening on 127.0.0.1:6666...
```

### 2. Start the Client

Open **Terminal 2** and run:

```bash
python client.py
```

Keep the server terminal open because the server must start before the client.

## Test Case 1: Lab Manual Input

Enter the following values in **Terminal 2 (Client)**:

```text
23
56
```

### Client Output

```text
Enter 1st no:
23
Enter 2nd no:
56
Numbers sent to server.
```

### Server Output

```text
Server listening on 127.0.0.1:6666...
Connected to client: ('127.0.0.1', 54321)
Received: 23, 56
Sum = 79
```

The client's port number may differ in the server output.

## Test Case 2: Additional Input

Enter the following values in **Terminal 2 (Client)**:

```text
145
255
```

### Server Output

```text
Received: 145, 255
Sum = 400
```

## Error Handling

- If the server is not running, the client displays:

  ```text
  Connection failed: Start server.py first.
  ```

- If non-integer values are entered, the client displays:

  ```text
  Invalid input: Enter integer numbers only.
  ```