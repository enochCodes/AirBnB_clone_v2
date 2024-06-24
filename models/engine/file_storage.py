#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import os
import json
from json.decoder import JSONDecodeError
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            return {k: v for k, v in self.__class__.__objects.items()
                    if type(v) is cls}
        return self.__class__.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None and hasattr(obj, "id"):
            cls_name = obj.__class__.__name__
            self.all()[f'{cls_name}.{obj.id}'] = obj

    def delete(self, obj=None):
        """delete obj from __objects"""
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in self.all():
                del self.all()[key]

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__class__.__file_path, "w") as f:
            dict_of_dicts = {}
            for key, value in self.__class__.__objects.items():
                dict_of_dicts[key] = value.to_dict()
            json.dump(dict_of_dicts, f)

    def reload(self):
        """Loads storage dictionary from file"""
        # We check if file exists otherwise error will be raised
        if os.path.isfile(self.__class__.__file_path):
            with open(self.__class__.__file_path, "r+") as f:
                try:
                    loaded_dict = json.load(f)
                    for key, value in loaded_dict.items():
                        cls_name = value.get("__class__")
                        obj = eval(cls_name)(**value)
                        self.new(obj)
                except JSONDecodeError:
                    json.dump({}, f)
        else:
            with open(self.__class__.__file_path, "w") as f:
                json.dump({}, f)
