%#!/usr/bin/python
""" holds class Activity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Activity(BaseModel, Base):
    """Representation of Activity """
    if models.storage_t == 'db':
        __tablename__ = 'activities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Activity"""
        super().__init__(*args, **kwargs)
