#!/usr/bin/python3

"""List all cities in a specific state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
    cursor = db.cursor()
    data = """SELECT cities.name
                 FROM states
                 INNER JOIN cities ON states.id = cities.state_id
                 WHERE states.name LIKE %s
                 ORDER BY cities.id ASC"""
    cursor.execute(data, (argv[4], ))

    print(', '.join(["{:s}".format(row[0]) for row in cursor.fetchall()]))

    db.close()
