#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from base_model.py import BaseModel


class User(BaseModel):
    """Insert personal details of the user"""
    def __init__(self, email, password, first_name, last_name):
        super().__init__()
        self.email = str(email)
        self.password = str(password)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
