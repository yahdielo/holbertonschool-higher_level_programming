#!/usr/bin/python3
'''Module provide a class that map to State table'''
# Module for Connecting To MySQL database
import sys

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''Class mapping table Sate'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))