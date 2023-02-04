import pickle

numEntries = int(input("Enter the number of new entries : "))
hotelData = []
for i in range(numEntries):
	roomno = input("Room no. : ")
	name = input("Name : ")
	duration = int(input("Duration : "))
	hotelData.append({"roomno": roomno, "name": name, "duration": duration})

with open("hotel.dat", "ab") as hotelFile:
	for i in hotelData:
		pickle.dump(i, hotelFile)

readData = []
with open("hotel.dat", "rb") as hotelFile:
	while True:
		try:
			readData.append(pickle.load(hotelFile))
		except EOFError:
			break

print("Data of each customer :")
for i in readData:
	print(i)

print("Number of customers :", len(readData))

print("Customers who have stays for more than 2 days :")
for i in readData:
	if i["duration"] > 2:
		print(i)
