#!/usr/bin/python3
"""
script that tests "Arizona'; TRUNCATE TABLE states ; SELECT *
FROM states WHERE name = '" as an input
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY ID ASC",
                (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
