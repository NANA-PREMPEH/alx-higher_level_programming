#!/usr/bin/python3
'''
script that takes in the name of a state as an argument and lists all cities
'''
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
            INNER JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name =  %s", [sys.argv[4]])

    rows = cur.fetchall()
    result = []
    for row in rows:
        result.append(row[0])

    print(', '.join(result))
    cur.close()
    db.close()
