#!/usr/bin/python3
"""
lists all states in database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    for i in cursor.fetchall():
        print(i)

    db.close()
