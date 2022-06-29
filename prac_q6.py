import csv

print("Data in file :")
with open("placement.csv", "r") as csvFile:
		for i in csv.reader(csvFile):
			print(i)

def NumApplicants():
	numApplicants = 0
	with open("placement.csv", "r") as csvFile:
		for i in csv.reader(csvFile):
			numApplicants += 1
	# no. of applicants does not include header
	print("No. of applicants :", numApplicants - 1)
NumApplicants()

def TopApplicants(numTopApplicants):
	readData = []
	with open("placement.csv", "r") as csvFile:
		for i in csv.reader(csvFile):
			readData.append(i)
	# ignore header
	readData = readData[1:]
	for i in range(len(readData)):
		totalMarks = int(readData[i][2]) + int(readData[i][3]) + int(readData[i][4]) + int(readData[i][5]) + int(readData[i][6])
		readData[i].append(totalMarks)
	readData.sort(key=lambda applicant: applicant[7], reverse = True)
	for i in range(numTopApplicants):
		print(readData[i])

numTopApplicants = int(input("Enter the number of top applicants : "))
print("Names of", numTopApplicants, "top applicants :")
TopApplicants(numTopApplicants)
