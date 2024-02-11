#!/usr/bin/python3
"""Edits how files are stored, seeializes and deserializes"""


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    self.__file_path
    self.__objects

    def all(self):
        """return __objects"""
        return __objects

    def new(self, obj):
        """Sets object with key"""
        <obj class name>.id

    def save(self):
        """serializes __objects to the JSON file"""
        save = JSON.dumps(__file_path)

    def reload(self):
        """deserializes JSON file if __file_path exists"""
        if __file_path is not None:
            reload = JSON.loads(save)
