#!/usr/bin/python3
"""
A script that lists all cities of a specified state from the database
hbtn_0e_4_usa. Results are sorted in ascending order by cities.id.
"""

import MySQLdb
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: ./5-filter_cities.py <mysql username> <mysql password> "
              "<database name> <state name>")
        return

    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_pass,
            db=db_name
        )
        cursor = db.cursor()
        
        query = (
            "SELECT cities.name FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC"
        )
        cursor.execute(query, (state_name,))
        rows = cursor.fetchall()
        
        if rows:
            print(", ".join(row[0] for row in rows))
        else:
            print()

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
