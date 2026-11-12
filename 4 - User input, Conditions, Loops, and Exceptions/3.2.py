my_list_numbers = [1, 3, 4, 8, 9, 5 ,9 ,2, 4 ,3, 2, 5]
for number in my_list_numbers:
    if number ==5:
        print(number*2)
    else:
        print(number)
my_x = [2, 4, 6, 8, 10]
my_y = [1, 3, 5 ,7]
for number in my_x:
    for number2 in my_y:
        print(number * number2)
dict_cisco = {'ports': 24, 'os': '18.1X1', 'device': '9600'}
print("Overzicht apparaat:")
for key, value in dict_cisco.items():
    print(key, value)
