#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_numerals = [
            ['I', 1], ['V', 5], ['X', 10], ['L', 50],
            ['C', 100], ['D', 500], ['M', 1000]
            ]
    num = 0
    value = 0
    for letter in roman_string:
        for numeral in roman_numerals:
            if letter == numeral[0]:
                if num == 0 or num >= numeral[1]:
                    value += numeral[1]
                elif num < numeral[1]:
                    value += numeral[1] - (num * 2)
                num = numeral[1]
    return value
