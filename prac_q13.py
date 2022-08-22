def stackStr(toProc):
    Stack = []
    for i in toProc:
        if i == "#" and len(Stack) > 0:
            Stack.pop()
        else:
            Stack.append(i)
    return Stack

def AreEqual(str1, str2):
    return stackStr(str1) == stackStr(str2)

inp1 = input("First string : ")
inp2 = input("Second string : ")

print(AreEqual(inp1,inp2))
