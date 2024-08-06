#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database
hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql_username> <mysql_password>"
              " <database_name>")
        sys.exit(1)

    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

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

        # Execute SQL query to retrieve states starting with 'N'
        cur.execute(
            "SELECT id, name FROM states WHERE name LIKE 'N%' "
            "ORDER BY id ASC"
        )

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
