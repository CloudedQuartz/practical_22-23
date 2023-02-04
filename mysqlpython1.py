import mysql.connector

MYSQLUSR = 'root'
MYSQLPASS = 'passwd'
mydb = mysql.connector.connect(host="localhost", user=MYSQLUSR, passwd=MYSQLPASS)
cursorObject = mydb.cursor()
cursorObject.execute("use mydb")


def addrecords():
	cursorObject.execute("USE mydb")
	sql = "INSERT INTO ITEM VALUES(%s,%s,%s)"
	x = input("Enter itemcode: ")
	y = input("Enter Itemname: ")
	z = float(input("Enter Price: "))
	val = (x, y, z)

	cursorObject.execute(sql, val)
	mydb.commit()


def showrec():
	Query = "SELECT * FROM ITEM"
	cursorObject.execute(Query)
	records = cursorObject.fetchall()
	for row in records:
		print(row)


def search():
	Q = "SELECT * FROM ITEM WHERE Itemcode = %s"
	s = input("Enter the item code: ")
	val = (s,)
	cursorObject.execute(Q, val)
	f = cursorObject.fetchall()
	for rows in f:
		print(rows)
while True:
	l = input("A: Add a record\nB: Show all records\nC: Search a record by itemcode\nChoice : ")
	match l.lower():
		case 'a':
			addrecords()
		case 'b':
			showrec()
		case 'c':
			search()
