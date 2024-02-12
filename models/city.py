#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from base_model.py import BaseModel


class City(BaseModel):
    """Gives the city and id of AirBnB"""
    def __init__(self, state_id, name):
        super().__init__()
        self.state_id = State.id
        self.name = name
