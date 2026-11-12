my_list = [5, 10, 15, 15, 10, 5]
my_set = {5, 10, 15, 15, 10, 5}
my_set2 = {5, 10, 20}
print(type(my_list))
print(type(my_set))
print(type(my_set2))
print(my_list)
print(my_set)
print(my_set2)
print(set(my_list))
print(len(my_set))
print(100 in my_set)
print(100 not in my_set)
print(5 in my_set)
my_set.add(20)
print(my_set)
my_set.remove(5)
print(my_set)
my_set.add(20)
print(my_set)
print(my_set.intersection(my_set2))
print(my_set.difference(my_set2))
print(my_set2.difference(my_set))
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_set = {6, 8, 2, 4, 12, 10}
my_new_set=set(my_list)
print(my_new_set)
print(my_set.intersection(my_new_set))
print(len(my_set))
my_set = {1, 2, 3, 4}
my_set=frozenset(my_set)
my_set.add(5)