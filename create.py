import sqlite3
connection = sqlite3.connect('sample.db') #':memory:' to create it in memory and dont store it
table = 'CREATE TABLE people (id integer primary key, name TEXT, surname TEXT)'
cursor = connection.cursor()
cursor.execute(table)
connection.commit()
