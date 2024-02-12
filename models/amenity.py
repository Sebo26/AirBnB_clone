#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from base_model.py import BaseModel


class Amenity(BaseModel):
    """Gives name of user"""
    def __init__(self, name):
        super().__init__()
        self.name = name
