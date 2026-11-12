my_numbers = [150, 125, 12, 6, 78, 30, 5, 12, 47, 1236]
for number in my_numbers:
    print(number)
else:
    print("Proficiat, uw for loop is met succes afgerond!")
for index, number in enumerate(my_numbers):
    print(index, number)
for number in my_numbers:
    print(number / 3)
my_new_numbers = []
for number in my_numbers:
    my_new_numbers.append(number)
my_new_numbers.sort()
print(my_new_numbers)