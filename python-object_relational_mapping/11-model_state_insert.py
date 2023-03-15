#!/usr/bin/python3
"""Start link class to table in database"""
import sys

from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    str1 = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(str1.format(sys.argv[1],
                                       sys.argv[2],
                                       sys.argv[3]), pool_pre_ping=True)

    session = sessionmaker(engine)
    session = session()
    states = session.query(State).all()
    lenght = len(states)

    new_state = State(id=lenght + 1, name='Louisiana')
    session.add(new_state)
    session.commit()

    result = session.query(State).filter(State.name == 'Louisiana')

    for item in result:
        print("{}".format(item.id))

    session.close()
