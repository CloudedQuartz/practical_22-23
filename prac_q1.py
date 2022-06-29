def WriteFile(fileName, text, mode):
	# mode = "a" or "w" for append or write
	if mode not in ["a", "w"]:
		return
	with open(fileName, mode) as file:
		file.write(text)

def ReadFile(fileName, readAsList):
	with open(fileName, "r") as file:
		if readAsList:
			fileData = file.readlines()
		else:
			fileData = file.read()
	return fileData

def GetLetterFreq(fileName):
	letterFreq = {}
	for i in ReadFile(fileName, False).split():
		char = i[0].lower()
		if ord(char) not in range(97, 123):
			# check if char is a letter
			continue
		if char not in letterFreq:
			letterFreq[char] = 1
		else:
			letterFreq[char] += 1
	return letterFreq

fileName = "file.txt"
writeText = "Neither apple nor pine are in pineapple. Boxing rings are square.\nWriters write, but fingers don't fing. Overlook and oversee are opposites.\nA house can burn up as it burns down. An alarm goes off by going on.\n"
WriteFile(fileName, writeText, "w")
print(ReadFile(fileName, False))

appendText = input("Enter text to append to file : ")
WriteFile(fileName, appendText, "a")

readList = ReadFile(fileName, True)
for i in range(len(readList)):
	readList[i] = str(i + 1) + ". " + readList[i]
	print(readList[i])
print("Last line :", ReadFile(fileName, True)[-1])
print("First line from 10th character on :", ReadFile(fileName, True)[0][9:])

lineNo = int(input("Line no. to be read : "))
print(ReadFile(fileName, True)[lineNo - 1])

print("Frequency of letters at the start of each word :")
print(GetLetterFreq(fileName))