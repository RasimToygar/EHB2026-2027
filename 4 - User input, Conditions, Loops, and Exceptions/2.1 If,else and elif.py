# Vraag het eerste getal
getal1 = int(input("Geef het eerste getal: "))
# Vraag het tweede getal
getal2 = int(input("Geef het tweede getal: "))
# Vraag de bewerking
bewerking = input("Welke bewerking (+, -, *, /): ")
# Controleer welke bewerking de gebruiker heeft gekozen
if bewerking == "+":
    print(getal1 + getal2)
elif bewerking == "-":
    print(getal1 - getal2)
elif bewerking == "*":
    print(getal1 * getal2)
elif bewerking == "/":
    print(getal1 / getal2)
else:
    print("Ongeldige bewerking")