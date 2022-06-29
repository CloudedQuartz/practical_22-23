import perfect

num = int(input("Enter a number : "))
print("Actions :")
print("1. Generate factors")
print("2. Check if number is prime")
print("3. Check if number is perfect")

action = int(input("Enter your choice : "))

if action == 1:
		print(perfect.generateFactors(num))
elif action == 2:
		print("Number is prime :", str(perfect.isPrimeNo(num)))
elif action == 3:
		print("Number is perfect :", str(perfect.isPerfectNo(num)))
