#!/usr/bin/python3
"""
A module defining a Student class.
"""


class Student:
    """
    A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given first name,
        last name, and age.

        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
            attrs (list, optional): A list of attribute names to retrieve.

        Returns:
            A dictionary containing the attributes of the Student instance.
        """
        if attrs is None or not isinstance(attrs, list) \
                or any(not isinstance(attr, str) for attr in attrs):
            return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on
        the provided JSON dictionary.

        Parameters:
            json (dict): A dictionary containing attribute names
                         and their corresponding values.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
