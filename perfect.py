'''
prac_q8 - perfect.py
'''
def generateFactors(num):
	factors = []
	for i in range(1, num + 1):
		if num % i == 0:
			factors.append(i)
	return factors

def isPrimeNo(num):
	print(generateFactors(num))
	if len(generateFactors(num)) <= 2:
		return True
	else:
		return False

def isPerfectNo(num):
	if sum(generateFactors(num)[:-1]) == num:
		return True
	else:
		return False
