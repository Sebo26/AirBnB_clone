#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """defines all common attributes/methods for other classes"""
    id = self.id = uuid.uuid4()
    self.created_at
    self.updated_at
    def __str__(self):
        """print unique id"""
        print f"[<class name>] (<self.id>) <self.__dict__>"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime()

    def to_dict(self):
        """returns dictionary, keys/values of __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        to_dict.to_json()
