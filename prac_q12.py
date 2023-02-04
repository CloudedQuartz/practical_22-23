Stack = []

def PopStack():
	return Stack.pop()

def AddToStack(num):
	tmpStack = []
	if len(Stack) > 0:
		while Stack[-1] > num:
			tmpStack.append(PopStack())
	Stack.append(num)
	for i in tmpStack[::-1]:
		Stack.append(i)

def DisplayStack():
	for i in Stack[::-1]:
		print(i)

print('Pick an action')
print('\t1. Display')
print('\t2. Add')
print('\t3. Exit')

while True:
	match int(input('Choice : ')):
		case 1:
			DisplayStack()
		case 2:
			num = int(input('Number to add : '))
			AddToStack(num)
		case 3:
			break