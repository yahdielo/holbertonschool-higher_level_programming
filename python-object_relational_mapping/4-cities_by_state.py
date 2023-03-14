#!/usr/bin/python3
""" This module quierys a nae starting with specific letter """

import sys

import MySQLdb


def matching_arg(argv):
    """
    Write a script that lists all cities from the database hbtn_0e_4_usa
    """

    conn = MySQLdb.connect(host="localhost",
                                port=3306, user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()

    db=sys.argv[3]
    # sql command to execute
    str1 = f"SELECT cities.id, cities.name, states.name FROM  cities INNER JOIN states ON cities.state_id = states.id"
    cur.execute(str1)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    matching_arg(sys)
