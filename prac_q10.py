def decimalToBinary(num):
	print(bin(num)[2:])

def decimalToOctal(num):
	print(oct(num)[2:])

def decimalToHex(num):
	print(hex(num)[2:])

usrInput = int(input("Enter the number : "))
operation = input("To convert into (B, O. H for binary, octal or hex) : ")

if operation == "B":
	decimalToBinary(usrInput)
elif operation == "O":
	decimalToOctal(usrInput)
elif operation == "H":
	decimalToHex(usrInput)