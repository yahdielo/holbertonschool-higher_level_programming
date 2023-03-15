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

    state = sys.argv[4]
    # sql command to execute
    str1 = "SELECT cities.name  FROM cities INNER JOIN states "
    str2 = f"ON cities.state_id = states.id WHERE states.name = '{state}'"
    cur.execute(str1+str2)

    query_rows = cur.fetchall()
    lenght = len(query_rows)
    index = 1

    for item in query_rows:

        print(item[0], end="")
        if index < lenght:
            print(", ", end="")
        index += 1
    print()
    cur.close()
    conn.close()


if __name__ == "__main__":
    matching_arg(sys)
