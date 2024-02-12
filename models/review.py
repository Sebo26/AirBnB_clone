#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from base_model.py import BaseModel


class Review(BaseModel):
    """Place and user id"""
    def __init__(self, place_id, user_id, text):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
