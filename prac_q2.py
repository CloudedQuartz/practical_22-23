def isvowel():
	with open("file1.txt", "r") as file1:
		readData = file1.read().split()
	writeData = []
	for i in readData:
		if i[0].lower() in ["a", "e", "i", "o", "u"]:
			continue
		else:
			writeData.append(i)
	writeData = " ".join(writeData)
	with open("file2.txt", "w") as file2:
		file2.write(writeData)

isvowel()