#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        cls_obj = {}
        # print("#######################################")
        # print(type(FileStorage.__objects))
        # print(cls, "<---Class")
        # print(FileStorage.__objects, "1111111111111111111111111")
        # print(FileStorage.__objects.keys(), "22222222")
        # print(FileStorage.__objects.items(), "333333333")
        # print("#########################################")
        for key , val in self.__objects.items():
            if isinstance(val, cls):
                cls_obj[key] =  val
        return cls_obj

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)
    def delete(self, obj=None):
        obj_to_del = None
        for key , val in self.__objects.items():
            if val is obj:
                obj_to_del = key
        if obj_to_del is not None:
            # print("***** object to del *****", obj_to_del)
            # print("Before delete",FileStorage.__objects)
            del FileStorage.__objects[obj_to_del]
            # print("after delete", FileStorage.__objects)
        
                
    

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
