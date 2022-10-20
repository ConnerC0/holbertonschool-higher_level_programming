#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """lists all the states in the table"""
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER by id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()