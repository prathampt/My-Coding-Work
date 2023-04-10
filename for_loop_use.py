
random_list = [35, "Pratham", 1.2, "Hello", 8, 12, 0.9, 79, "Name", 78]
my_list1 = []
my_list2 = []

#1
for item in random_list:
    if type(item) == str:
        pass
    else:
        if item < 6:
            pass
        else:
            my_list1.append(item)

#2
for item in random_list:
    if str(item).isnumeric() and item>=6:
        my_list2.append(item)

    
print(my_list1)
print(my_list2)
