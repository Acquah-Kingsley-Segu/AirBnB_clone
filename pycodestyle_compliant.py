#!/usr/bin/python3
"""
    Contains a simple class code that passes pycodestyle checker
"""


class Person:
    """ Creates a Person class template """
    def __init__(self, name):
        """ Instantiates the object by taking name of object
            Args:
                name (str): contains full name of instance object
        """
        self.name = name

    def introduce(self):
        """ Introduces the instance object """
        print(f"Hello, my name is {self.name}")

person = Person("Acquah Kingsley Segu")
person.introduce()
