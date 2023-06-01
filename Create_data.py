## =  +

import sqlite3

CREATE_BEANS_TABLE =  "CREATE TABLE iIF NOT EXIST beans (id INTEGER PRIMARY KEY, name TEXT, methord TEXT, rating INTEGER);" 

INSERT_BEAN = "INSERT INTO bean (name, methord,rating) VALUE (?,?,?);"

GET_ALL_BEAN ="SELECT * FROM BEAN;"
GET_BEAN_BY_NAME = "SELECT*FROM beans WHERE name = ?;"
GET_BEST_PREPARETION_FOR_BEAN =""""
SELECT * FROM beans
WHERE name = ?
ORDER BY rating DEC
LIMIT 1;
"""

def connect():
  return sqlite3.connect('data.db')

def creat_tables(connection):
 with connection:
    connection.execute(CREATE_BEANS_TABLE)


def add_bean(connection,name, methord, rating):
   with connection:
     connection.execute(INSERT_BEAN, (name,methord, rating))


def get_all_beans(connection):
 with connection:
   return connection.execute(GET_ALL_BEAN).fetchall()



def get_beans_by_name(connection, name):
 with connection:
   return connection.execute(GET_BEAN_BY_NAME).fetchall()

def get_best_preparetion_for_bean(connection, name):
  with connection:
    return connection.execute (GET_BEST_PREPARETION_FOR_BEAN,(name,)).fetchone()