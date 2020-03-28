#!/usr/bin/python3
"""This file conect an DB and make a query"""

import MySQLdb
import sys

if __name__ = "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[2],
                         passwd=sys.argv[1],
                         db=sys.argv[3])
    cur = db.cursor()

    # Execute the query
    cur.execute('SELECT id, name FROM states ORDER BY id ASC;')
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
