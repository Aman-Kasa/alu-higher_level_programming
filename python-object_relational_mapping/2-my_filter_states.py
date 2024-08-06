#!/usr/bin/python3
"""
Lists all states in the states table where the name matches the given argument.
"""
import MySQLdb
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> "
              "<database_name> <state_name>")
        sys.exit(1)

    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=passwd,
            db=dbname
        )

        # Create a cursor object
        cur = db.cursor()

        # Execute SQL query with user input
        query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

        # Fetch and print results
        for row in cur.fetchall():
            print(row)

        # Close cursor and database connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
