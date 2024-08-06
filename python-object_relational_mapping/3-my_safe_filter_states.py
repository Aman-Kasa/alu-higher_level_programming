#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, using parameterized
queries to prevent SQL injection.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <mysql username> "
              "<mysql password> <database name> <state name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
