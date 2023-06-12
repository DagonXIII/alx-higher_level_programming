#!/usr/bin/python3

MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

with open('tests/1-my_list.txt', 'w') as file:
    file.write(str(my_list) + '\n')
    my_list.print_sorted()
    file.write(str(my_list) + '\n')
