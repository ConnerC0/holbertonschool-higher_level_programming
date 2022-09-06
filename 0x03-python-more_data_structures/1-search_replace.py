#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def search_replace_i(i):
        return (i if i != search else replace)
    return list(map(search_replace_i, my_list))
