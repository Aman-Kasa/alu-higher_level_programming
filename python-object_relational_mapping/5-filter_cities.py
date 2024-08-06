#!/usr/bin/python3
"""
A script that lists all cities of a specified state from the database 
hbtn_0e_4_usa. Results are sorted in ascending order by cities.id.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./5-filter_cities.py <mysql username> <mysql password> "
              "<database name> <state name>")
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

    # Query to get the state id based on the state name
    query = "SELECT id FROM states WHERE name = %s"
    cursor.execute(query, (state_name,))
    state_id = cursor.fetchone()

    if state_id is None:
        print()
        cursor.close()
        db.close()
        sys.exit(0)

    state_id = state_id[0]

    # Query to get cities for the state_id
    query = "SELECT name FROM cities WHERE state_id = %s ORDER BY id ASC"
    cursor.execute(query, (state_id,))
    results = cursor.fetchall()

    # Print cities in a comma-separated format
    print(", ".join(row[0] for row in results))

    cursor.close()
    db.close()
