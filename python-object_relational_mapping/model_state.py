#!/usr/bin/python3

"""Start link class to table in database
"""
import sys

from sqlalchemy import Column, Integer, String, create_engine

from model_state import Base, State

if __name__ == "__main__":
    str1 = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine({str1}.format(sys.argv[1],
                                         sys.argv[2],
                                         sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)


class State(Base):
    """ State class inherits from Base and is linked to mysqlalchemy """

    __tablename__ = 'states'
    id = Column(integer, primarykey=True)
    name = Column(String(128))
