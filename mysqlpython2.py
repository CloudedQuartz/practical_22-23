import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwd")
cursorObject = mydb.cursor()
cursorObject.execute("use mydb")


def addrecords():
	cursorObject.execute("USE mydb")
	sql = "INSERT INTO Student VALUES(%s,%s,%s,%s,%s)"
	l = int(input("Enter Rollno: "))
	k = input("Enter Name: ")
	z = int(input("Enter Class: "))
	a = input("DOB YYYY-MM-DD: ")
	b = input("Gender M/F/O: ")

	val = (l, k, z, a, b)

	cursorObject.execute(sql, val)
	mydb.commit()


def updaterecord():
	cursorObject.execute("USE mydb")
	x = input(
		"""What do you wish to update: 
	1.Name
	2.Class
	3.DOB
	4.Gender : """
	)
	if x == "1":
		y = "Name"
		c = input("Enter Name: ")
		sql = "UPDATE Student SET Name = %s WHERE Rollno = %s"
	elif x == "2":
		y = "Class"
		c = int(input("Enter Class: "))
		sql = "UPDATE Student SET Class = %s WHERE Rollno = %s"
	elif x == "3":
		y = "DOB"
		c = input("DOB YYYY-MM-DD: ")
		sql = "UPDATE Student SET DOB = %s WHERE Rollno = %s"
	elif x == "4":
		y = "Gender"
		c = input("Gender M/F/O: ")
		sql = "UPDATE Student SET Gender = %s WHERE Rollno = %s"
	f = int(input("Enter the rollnumber: "))
	val = (c,f)
	cursorObject.execute(sql,val)
	mydb.commit()


while True:
	x = input(
		"""What do you wish to do?
	1. add a record
	2. update a record : """
	)
	if x == "1":
		addrecords()
	elif x == "2":
		updaterecord()
