#!/usr/bin/python3
"""
This script takes in an argument
and displays all values in the 
states where `name` matches the
argument from the db `hbtn_0e_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Acess to the db and get the
    state.
    """

    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
