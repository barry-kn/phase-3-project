import sqlite3


connection  = sqlite3.connect('data.db')

with connection:
    connection.execute(
        "CREATE TABLE  (id INTEGER PRIMARY KEY, name TEXT, methord TEXT, rating INTEGER);"  "
    )
    