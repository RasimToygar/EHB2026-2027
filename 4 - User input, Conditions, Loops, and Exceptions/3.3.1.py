network_packets = [
{"source": "192.168.1.1", "destination": "192.168.1.20", "size": 1500},
{"source": "123.47.36.9", "destination": "23.178.65.2", "size": 900},
{"source": "192.168.1.1", "destination": "192.168.1.42", "size": 1200},
{"source": "94.123.5.7", "destination": "184.14.23.1", "size": 800},
{"source": "192.168.1.2", "destination": "192.168.1.47", "size": 700},
{"source": "192.168.1.2", "destination": "168.4.1.7", "size": 700},
]
large_packets = 0
internal_traffic = 0
external_traffic = 0
for packet in network_packets:
    print("Packet met als source:", packet["source"])
    print("Packet met als destination:", packet["destination"])
    print("Packet met als packet-size:", packet["size"])
    if packet["size"] > 1000:
        print("Packet-size is groter dan 1000.\n")
        large_packets += 1