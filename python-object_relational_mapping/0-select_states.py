#!/usr/bin/python3
""" 
    This module takes 3 arguments from the terminal and connects to mysqldb
    then lists all states from the data base
"""
import sys

import MySQLdb


def states(argv):
    ''' Thos module is documented '''

    conn = MySQLdb.connect(host = "localhost", port = 3306, user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

states(sys)

