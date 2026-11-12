my_answer = input("Waarvoor gebruik je internet explorer? ")
if len(my_answer) >= 20:
    print(my_answer)
check_me = "Netmiko Al Van Gehoord?"
my_ending = "Eindigt deze zin nu op een uitroepteken ?!"
if "A" in check_me and check_me.count("o") >= 3:
    print("Gevonden")
else:
    print("Neen nog niet gehoord")
my_ending = "Eindigt deze zin nu op een uitroepteken ?!"
if my_ending.endswith("!"):
    print("Eindigt met een uitroepteken")
else:
    print("Neen eindigt niet op een uitroepteken")
my_vendors = {1: "Cisco", 2: "Huawei", 3: "Juniper", 4: "Ruckus"}
if 4 in my_vendors and "c" in my_vendors[4]:
    print("Gevonden")
else:
    print("Neen nog niet gehoord")

