#!/usr/bin/python3
def print_list_integer(my_list=[]):
    string = ['{}'.format(x) for x in my_list]
    for x in range(len(my_list)):
            print(my_list[x])
