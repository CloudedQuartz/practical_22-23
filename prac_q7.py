def count(n):
	numDigits = 0
	while n > 0:
		n //= 10
		numDigits += 1
	print("Number of digits =", numDigits)

def reverse(n):
	reversedNum = 0
	while n > 0:
		digit = n % 10
		reversedNum = reversedNum * 10 + digit
		n //= 10
	print("Reversed number =", reversedNum)

def hasdigit(n):
	checkDigit = int(input("Digit to check : "))
	while n > 0:
		digit = n % 10
		if digit == checkDigit:
			print("Digit is present.")
			return
		n //= 10

	print("Digit is not present.")

def show(n):
	nOrig = n
	placeVal = []
	i = 1
	while n > 0:
		placeVal.append((n % 10) * i)
		n //= 10
		i *= 10
	print(nOrig, "=", end = " ")
	print(*placeVal, sep = " + ")

num = int(input("Enter the number : "))
count(num)
reverse(num)
hasdigit(num)
show(num)
