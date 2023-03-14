#!/usr/bin/python3
""" This module quierys a nae starting with specific letter """

import sys

import MySQLdb


def matching_arg(argv):
    """
    This module quierys a name matching argmunet index 4,
    write one that is safe from MySQL injections!
    """

    conn = MySQLdb.connect(host="localhost",
                                port=3306, user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()

    arg_name = (sys.argv[4], )
    # sql command to execute
    str1 = "SELECT * FROM  states WHERE NAME LIKE BINARY %s"
    cur.execute(str1, arg_name)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    matching_arg(sys)
