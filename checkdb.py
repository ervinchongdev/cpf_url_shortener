import sqlite3
con = sqlite3.connect('database.db')

cur = con.cursor()

for row in cur.execute('SELECT * from urls'):
	print(row)
