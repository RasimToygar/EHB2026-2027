my_lower = input("Wat is je secret voor kleine letters? ")
my_upper = input("Wat is je secret voor hoofdletters? ")
my_digit = input("Wat is je secret voor getallen? ")
if not my_lower.islower():
    print("Fout gebruik kleine letters")
if not my_digit.isdigit():
    print("Fout: gebruik cijfers")
if len(my_lower) < 8:
    print("Fout: de code moet minstens 8 tekens bevatten")
else:
    print("De code heeft voldoende tekens")
