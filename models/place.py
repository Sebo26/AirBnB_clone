#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from base_model.py import BaseModel


class Place(BaseModel):
    """Details about the location"""
    def __init__(self, city_id, user_id, name, description, number_rooms):
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms

