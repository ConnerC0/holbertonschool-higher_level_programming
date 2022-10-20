#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """


import MySQLdb
import sys

def select_states():
	"""lists all the states in the table"""
	conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                               passwd=sys.argv[2], database=sys.argv[3])

	cur = conn.cursor()

	cur.execute("SELECT * FROM states ORDER by id ASC")
	rows = cur.fetchall()
	for row in rows:
		print(row)

	cur.close()
	conn.close()

if __name__ == "__main__":
	select_states()
