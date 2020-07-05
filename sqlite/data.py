import sqlite3

conn = sqlite3.connect('squad.db')
# create cursor
c = conn.cursor()

# create a table
# c.execute("""CREATE TABLE customer (
#         first_n text,
#         last_n text,
#         gmail text
# )""")

# many_customers = [
#     ('barath', 'viknesh', 'barathviknesh.9566@gmail.com'),
#     ('viki', 'downey', 'vikiind@gmail.com'),
#     ('bharath', 'vignesh', 'barathviknesh.a6000@gmail.com')
# ]


# c.executemany(
#     """INSERT INTO customer VALUES (?,?,?)""", many_customers)


# c.execute("SELECT rowid, * FROM customer WHERE last_n='viknesh' ")


#update records
# c.execute("""UPDATE customer SET first_n ='viki'
# 	          WHERE last_n ='downey'
#  """)
#delete
# c.execute("""DELETE from customer WHERE rowid = 3 
# 	""")
# conn.commit()

#query the db order by
# c.execute("SELECT rowid, * FROM customer ORDER BY rowid DESC")
#AND AND OR
# c.execute("SELECT rowid, * FROM customer WHERE last_n LIKE 'vi%' AND rowid = 4")

# c.execute("SELECT rowid, * FROM customer LIMIT 2")

c.execute("SELECT rowid, * FROM customer ORDER BY rowid DESC LIMIT 2")
#delete table
# c.execute("DROP TABLE ")
# conn.commit()
#query the database
# c.execute("SELECT * FROM customer")

items=c.fetchall()

for item in items:
	# print(item[0] + " " + item[1] +" \t\t" + item[2])
	print(item)
print("it works")
# commited command
conn.commit()
# close our connection
conn.close()
