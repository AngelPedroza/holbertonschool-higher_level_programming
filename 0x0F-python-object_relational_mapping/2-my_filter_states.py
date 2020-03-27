#!/usr/bin/python3

import MySQLdb
import sys


db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=sys.argv[2],
                     passwd=sys.argv[1],
                     db=sys.argv[3])

cur = db.cursor()

# Execute the query
query = "SELECT id, name FROM states WHERE name='{}' ORDER BY id ASC;".format(
    sys.argv[4])
cur.execute(query)

for row in cur.fetchall():
    print(row)

cur.close();
db.close()
