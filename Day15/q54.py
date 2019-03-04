# Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

__author__ = "Mahtab Alam"

class IOstring:
    def __init__(self):
        self.str = ""

    def get_string(self):
        self.str = input()

    def print_string(self):
        print(self.str.upper())


string = IOstring()
string.get_string()
string.print_string()
