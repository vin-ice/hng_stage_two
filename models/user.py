#!/usr/bin/python3
"""User storage Model"""
import models
from uuid import uuid4


class User:
    def __init__(self, name=None, value=None, **kwargs):
        self.name = name
        self.value = value
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
        if not hasattr(self, 'user_id'):
            self.user_id = str(uuid4())

    def delete(self):
        """deletes user"""
        models.store.delete("users", self)

    def save(self):
        """saves user object to storage"""
        models.store.new("users", self)

    def update(self):
        """saves the updated values"""
        models.store.update("users", self)

    def to_dict(self):
        new_dict = self.__dict__.copy()
        if 'id' in new_dict.keys():
            del new_dict['id']
        return new_dict

    @staticmethod
    def from_store(user_id: str = None):
        """retrieves a user and models them appropriately"""
        record = models.store.get("users", user_id=user_id)
        if record:
            return User(**dict(zip(('id', 'user_id', 'name', 'value'),
                               record)))
        else:
            return None
