
# Experiment No. 07
# WAP to Implement Name Resolution Protocol

class NameResolver:
    def __init__(self):
        # Sample DNS records
        self.records = {
            "example.com": "192.0.2.1",
            "openai.com": "192.0.2.2",
            "google.com": "192.0.2.3"
        }
        self.cache = {}

    # Forward Lookup: Hostname to IP
    def resolve(self, hostname):
        hostname = hostname.lower()

        if hostname in self.cache:
            print("Cache hit for", hostname)
            return self.cache[hostname]

        print("Cache miss for", hostname)
        ip_address = self.records.get(hostname)

        if ip_address is not None:
            self.cache[hostname] = ip_address

        return ip_address

    # Reverse Lookup: IP to Hostname
    def reverse_resolve(self, ip_address):
        for hostname, address in self.records.items():
            if address == ip_address:
                return hostname

        return None


if __name__ == "__main__":
    resolver = NameResolver()

    # Forward Lookup
    print("Forward Lookup:")

    hostnames = [
        "example.com",
        "openai.com",
        "google.com",
        "not_exist.com",
        "example.com"
    ]

    for hostname in hostnames:
        ip = resolver.resolve(hostname)

        if ip is not None:
            print(hostname, "->", ip)
        else:
            print(hostname, "does not exist")

    # Reverse Lookup
    print("\nReverse Lookup:")

    ip_address = "192.0.2.2"
    hostname = resolver.reverse_resolve(ip_address)

    if hostname is not None:
        print(ip_address, "->", hostname)
    else:
        print(ip_address, "does not exist")
