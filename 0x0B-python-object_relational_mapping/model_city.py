#!/usr/bin/python3
"""
module for city class
"""


import sqlalchemy
from sqlalchemy import Column, Integer, STring, ForeignKey
from model_state import Base, State

class City(Base):
    """rep of city class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
