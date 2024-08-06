#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database
hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def main():
    if len(sys.argv) != 4:
        msg = ("Usage: ./1-filter_states.py <mysql_username> "
               "<mysql_password> <database_name>")
        print(msg)
        sys.exit(1)

    user, passwd, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost", port=3306, user=user,
            passwd=passwd, db=dbname
        )
        cur = db.cursor()
        cur.execute(
            "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        )
        for row in cur.fetchall():
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
