#!/usr/bin/python3
"""

Script ot list all filtered states with a name starting with N

"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the db and get starting with N
    """
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%'"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
