#!/usr/bin/python3

""" A File Storage module """


import json

class FileStorage():
    """ Implements a file storage concept """


    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns all objects created so far """


        return self.__objects

    def new(self, obj):
        """ Adds a new object to the __object class instance """
        

        key = f"BaseModel.{obj['id']}"
        self.__objects[key] = obj
        self.__objects[key]['created_at'] = self.__objects[key]['created_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__objects[key]['updated_at'] = self.__objects[key]['updated_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")

    def save(self):
        """ Saves the contents in __objects to a file """


        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        try:
             with open(self.__file_path, "r") as f:
                 self.__objects = json.load(f)
        except:
            pass



