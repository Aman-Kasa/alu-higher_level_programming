#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> "
              "<database_name>")
        sys.exit(1)

    # Get MySQL credentials and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve all states
        cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

        # Fetch all the rows from the executed query
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error {e}")
        sys.exit(1)
