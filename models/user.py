#!/usr/bin/python3
"""Class that inherits from BaseModel"""


class User(BaseModel):
    """Insert personal details"""
    email = str(email)
    password = str(password)
    first_name = str(first_name)
    last_name = str(last_name)
