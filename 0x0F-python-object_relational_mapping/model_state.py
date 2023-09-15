#!/usr/bin/python3

"""Class State"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, UniqueConstraint, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class State"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(length=128), nullable=False)
