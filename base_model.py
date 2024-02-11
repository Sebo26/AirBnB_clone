#!/usr/bin/python3
from datetime import datetime

class BaseModel:
    """defines all common attributes/methods for other classes"""
    id = self.id = uuid.uuid4()
    self.created_at
    self.updated_at
    def __str__(self):
        """print unique id"""
        print "[<class name>] (<self.id>) <self.__dict__>"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        updated_at = datetime()

    def to_dict(self):
        """returns dictionary, keys/values of __dict__"""
        self.__dict__
        to_dict.append(__class__)
        created_at_isoformat = created_at.isoformat()
        updated_at_isoformat = updated_at.isoformat()
        to_dict.to_json()
