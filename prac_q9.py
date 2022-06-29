romToNum = {
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000,
}

def romToDec(roman):
	decimal = 0
	i = 0
	lenRom = len(roman)
	while i + 1 < lenRom:
		if romToNum[roman[i]] < romToNum[roman[i + 1]]:
			decimal += romToNum[roman[i + 1]] - romToNum[roman[i]]
			i += 1
		else:
			decimal += romToNum[roman[i]]
		i += 1
	if i < lenRom:
		decimal += romToNum[roman[-1]]
	print(decimal)

roman = input("Enter the roman numeral : ")
romToDec(roman)