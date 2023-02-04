def reshape(mat, r, c):
	if len(mat[0]) * len(mat) != r * c:
		print("Incompatible output parameters.")
		print(mat)
		return
	matTemp = []
	for i in mat:
		for j in i:
			matTemp.append(j)
	matNew = []
	k = 0
	while k < len(matTemp):
		for i in range(r):
			matNew.append([])
			for j in range(c):
				matNew[i].append(matTemp[k])
				k += 1
	for i in matNew:
		print(i)
matSizeOrig = input("Original matrix size as 'm x n' : ").replace(" ", "").replace("X", "x").split("x")

matOrig = []
for i in range(int(matSizeOrig[0])):
	matOrig.append([])
	for j in range(int(matSizeOrig[1])):
		print("Row :", i + 1, "Column :", j + 1)
		matOrig[i].append(int(input("Value : ")))

matSizeNew = input("Output matrix size as 'm x n' : ").replace(" ", "").replace("X", "x").split("x")

reshape(matOrig, int(matSizeNew[0]), int(matSizeNew[1]))
