network_devices = [
{"name": "Router 1", "status": "Up"},
{"name": "Switch 1", "status": "Down"},
{"name": "Firewall 1", "status": "Down"},
{"name": "Server 1", "status": "Up"},
{"name": "switch 2", "status": "Down"}
]
for device in network_devices:
    print("Status van apparaat:", device["name"])
    if device["status"] == "Up":
        print("Apparaat:", device["name"], "is operationaal. Er zijn geen acties nodig.")
    elif device["status"] == "Down":
        print("Apparaat:", device["name"], "is niet operationaal. Enkele acties zijn nodig.")
        device["status"] = "Up"
    else:
        print("Status is ongekend.")
print("De status van alle apparaten:")
for device in network_devices:
    print("Naam apparaat:", device["name"])
    print("Status apparaat:", device["status"])
