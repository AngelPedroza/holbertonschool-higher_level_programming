#!/usr/bin/python3
"""Query SQL injection safe"""
import MySQLdb
import sys


db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=sys.argv[2],
                     passwd=sys.argv[1],
                     db=sys.argv[3])

cur = db.cursor()

# Execute the query
query = """SELECT id, name FROM states WHERE name = %s ORDER BY id ASC;"""
cur.execute(query, (sys.argv[4], ))

for row in cur.fetchall():
    print(row)

cur.close()
db.close()
