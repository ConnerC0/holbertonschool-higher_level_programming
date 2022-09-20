#!/usr/bin/python3
""" task 10 student to JSON """


class Student:
    """ student class """
    def __init__(self, first_name, last_name, age):
        """ initialization method """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns dictionary represetnation of student instance """
        ClassDict = vars(self)
        MethodDict = {}

        if attrs is None:
            return ClassDict

        for a in attrs:
            if a in ClassDict:
                MethodDict[a] = ClassDict[a]
        return MethodDict
