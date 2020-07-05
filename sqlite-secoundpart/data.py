import sqlite3

#query db and return all records
def show_all():
	#connect to database
	conn = sqlite3.connect('squad.db')
	# create cursor
	c = conn.cursor()
	#query
	c.execute("SELECT rowid,* FROM customer")
	items=c.fetchall()
	for item in items:
		print(item)
	print("fromshowall")
	# commited command
	conn.commit()
	# close our connection
	conn.close()

#add a new record to the table
def add_one(first,last,email):
	#connect to database
	conn = sqlite3.connect('squad.db')
	# create cursor
	c = conn.cursor()
	#query
	c.execute("INSERT INTO customer VALUES (?,?,?)", (first, last, email)) 
	#print
	print("from addone")
	# commited command
	conn.commit()
	# close our connection
	conn.close()


#add many a new record to the table
def add_many(list):
	#connect to database
	conn = sqlite3.connect('squad.db')
	# create cursor
	c = conn.cursor()
	#query
	c.executemany("INSERT INTO customer VALUES (?,?,?)", (list) )
	#print
	print("from addmany")
	# commited command
	conn.commit()
	# close our connection
	conn.close()


#delete record from table
def delete_one(id):
	#connect to database
	conn = sqlite3.connect('squad.db')
	# create cursor
	c = conn.cursor()
	#query
	c.execute("DELETE from customer WHERE rowid =(?)", id)
	#print
	print("from delete_one")
	# commited command
	conn.commit()
	# close our connection
	conn.close()

#where
def look_up(gmail):
	#connect to database
	conn = sqlite3.connect('squad.db')
	# create cursor
	c = conn.cursor()
	#query
	c.execute("SELECT rowid, * from customer WHERE gmail =(?)", (gmail,))
	items=c.fetchall()
	for item in items:
		print(item)
	#print
	print("from lokup")
	# commited command
	conn.commit()
	# close our connection
	conn.close()


