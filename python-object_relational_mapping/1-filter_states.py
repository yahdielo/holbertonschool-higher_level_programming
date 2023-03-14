#!/usr/bin/python3
""" This module quierys a nae starting with specific letter """

import sys

import MySQLdb


def start_letter(argv):
    """ This module quierys a nae starting with specific letter """

    conn = MySQLdb.connect(host="localhost",
                                port=3306, user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()

    # sql command to execute
    var1 = f"SELECT * FROM  states WHERE NAME LIKE BINARY 'N%' ORDER BY states.id ASC"
    cur.execute(var1)

    query_rows = cur.fetchall()

    for row in query_rows:S
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    start_letter(sys)
