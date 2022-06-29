fileName = "data.txt"
with open(fileName, "r") as file:
	fileData = file.read().split("\n")

fileDataList = []
for i in fileData:
	fileDataList.append(tuple(i.split("\t")))

fileDataList.sort(key = lambda student: int(student[2]))
print("Students with less than 3 years :")
for i in fileDataList:
	if int(i[3]) < 3:
		print(i)

print("No. of people in each dept.")
deptFreq = {}
for i in fileDataList:
	if i[4] not in deptFreq:
		deptFreq[i[4]] = 1
	else:
		deptFreq[i[4]] += 1
print(deptFreq)