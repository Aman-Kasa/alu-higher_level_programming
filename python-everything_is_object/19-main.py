#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

# Test cases
my_list1 = [1, 2, 3]
my_list2 = [1]
my_list3 = [1, "2", 3]
my_list4 = [1, [2, 3], {'id': 12}]
my_list5 = []

# Testing the function
new_list1 = copy_list(my_list1)
new_list2 = copy_list(my_list2)
new_list3 = copy_list(my_list3)
new_list4 = copy_list(my_list4)
new_list5 = copy_list(my_list5)

# Printing original and copied lists
print(my_list1)
print(new_list1)
print()
print(my_list2)
print(new_list2)
print()
print(my_list3)
print(new_list3)
print()
print(my_list4)
print(new_list4)
print()
print(my_list5)
print(new_list5)

# Comparing lists
print(new_list1 == my_list1)
print(new_list2 == my_list2)
print(new_list3 == my_list3)
print(new_list4 == my_list4)
print(new_list5 == my_list5)

# Comparing identities
print(new_list1 is my_list1)
print(new_list2 is my_list2)
print(new_list3 is my_list3)
print(new_list4 is my_list4)
print(new_list5 is my_list5)
