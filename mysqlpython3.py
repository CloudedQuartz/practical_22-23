import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
cursorObject = mydb.cursor()
cursorObject.execute("use mydb")

def addrecords():
    cursorObject.execute("USE mydb")
    sql = "INSERT INTO BUS VALUES(%s,%s,%s,%s,%s)"
    l = int(input("Enter bus no: "))
    k = input("Enter origin : ")
    a = input("DEnter Destination: : ")
    z = float(input("Enter rate: "))    
    b = float(input("Enter Km Number: "))

    val = (l, k, a, z, b)

    cursorObject.execute(sql, val)
    mydb.commit()

def displaydetails():
    cursorObject.execute("USE mydb")
    sql = "SELECT * FROM BUS"
    cursorObject.execute(sql)
    f = cursorObject.fetchall()
    for row in f:
        print(row)

while True:
    x = input("""WHAT DO YOU WISH TO DO?
    1. ADD A NEW RECORD
    2. DISPLAY DETAILS  : """)
    if x == '1':
        addrecords()
    elif x == '2':
        displaydetails()
