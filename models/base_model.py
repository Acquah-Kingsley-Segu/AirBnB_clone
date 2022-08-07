#!/usr/bin/python3

from datetime import datetime
import uuid
"""
    Contains a base class definition for all classes to be used in this project
"""


class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        to_dict = self.__dict__
        to_dict['created_at'] = to_dict['created_at'].strftime("%Y-%m-%dT%H:%M%S.%f")
        to_dict['updated_at'] = to_dict['updated_at'].strftime("%Y-%m-%dT%H:%M%S.%f")
        to_dict['__class__'] = 'BaseModel'

        return to_dict
