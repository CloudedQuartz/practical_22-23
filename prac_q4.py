with open("myfile.txt", "r") as myFile:
	fileData = myFile.read()

cleanFileData = ""
# change \n to space for easier handling and splitting
fileData.replace("\n", " ")
for i in fileData:
	# clean punctuation marks and numbers
	if i.isalpha() or i == " ":
		cleanFileData += i

wordFreq = {}
for i in cleanFileData.split():
	i = i.lower()
	if i not in wordFreq:
		wordFreq[i] = 1
	else:
		wordFreq[i] += 1
print(wordFreq)