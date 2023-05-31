## =  +

import sqlite3

def connect():
  return sqlite3.connect('data.db')

def creat_tables(connection):
 with connection:
    connection.execute(
        "CREATE TABLE  (id INTEGER PRIMARY KEY, name TEXT, methord TEXT, rating INTEGER);" 
    )
    