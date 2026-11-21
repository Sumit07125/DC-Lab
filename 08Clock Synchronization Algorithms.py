# Experiment No. 8: WAP to implement Clock Synchronization Algorithms (Berkeley Algorithm)

def parse_time(time_str: str) -> int:
    """Convert 'mm:ss' string into total seconds."""
    parts = time_str.strip().split(":")
    if len(parts) != 2:
        raise ValueError("Time must be in mm:ss format (e.g., 07:23)")
    minutes, seconds = int(parts[0]), int(parts[1])
    if minutes < 0 or not (0 <= seconds < 60):
        raise ValueError("Minutes must be >= 0 and seconds must be between 00 and 59")
    return minutes * 60 + seconds


def format_time(total_seconds: float) -> str:
    """Convert total seconds back into 'mm:ss' format."""
    sec = int(total_seconds) % 3600
    minutes = sec // 60
    seconds = sec % 60
    return f"{minutes:02d}:{seconds:02d}"


def berkeley_algorithm(server_time: str, client1_time: str, client2_time: str) -> None:
    print(f"\nServer Clock   = {server_time}")
    print(f"Client Clock 1 = {client1_time}")
    print(f"Client Clock 2 = {client2_time}")

    # Convert clock strings to seconds
    s = parse_time(server_time)
    t1 = parse_time(client1_time)
    t2 = parse_time(client2_time)

    # Calculate time difference between each client and the server
    st1 = t1 - s
    st2 = t2 - s
    print(f"t1 - s = {st1}")
    print(f"t2 - s = {st2}")

    # Compute average time difference
    avg = (st1 + st2) / 2
    print(f"(st1 + st2) / 2 = {int(avg)}")

    # Compute adjustments for server and clients
    adj_server = avg
    adj_t1 = avg - st1
    adj_t2 = avg - st2
    print(f"Server adjustment   = {int(adj_server)}")
    print(f"Client 1 adjustment = {int(adj_t1)}")
    print(f"Client 2 adjustment = {int(adj_t2)}")

    # Synchronize all clocks
    sync_server = s + adj_server
    sync_t1 = t1 + adj_t1
    sync_t2 = t2 + adj_t2

    print(f"\nSynchronized Server Clock   = {format_time(sync_server)}")
    print(f"Synchronized Client 1 Clock = {format_time(sync_t1)}")
    print(f"Synchronized Client 2 Clock = {format_time(sync_t2)}")


if __name__ == "__main__":
    try:
        server_input = input("Enter Server Time (mm:ss): ")
        client1_input = input("Enter Client 1 Time (mm:ss): ")
        client2_input = input("Enter Client 2 Time (mm:ss): ")
        berkeley_algorithm(server_input, client1_input, client2_input)
    except ValueError as err:
        print(f"Invalid input: {err}")



#Output:Enter Server Time (mm:ss): 07:23
# Enter Client 1 Time (mm:ss): 3:50
# Enter Client 2 Time (mm:ss): 6:45

# Server Clock   = 07:23
# Client Clock 1 = 3:50
# Client Clock 2 = 6:45
# t1 - s = -213
# t2 - s = -38
# (st1 + st2) / 2 = -125
# Server adjustment   = -125
# Client 1 adjustment = 87
# Client 2 adjustment = -87

# Synchronized Server Clock   = 05:17
# Synchronized Client 1 Clock = 05:17
# Synchronized Client 2 Clock = 05:17