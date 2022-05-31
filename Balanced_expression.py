top = -1
stack = []
exp = input("Enter your expression: ")
def isEmpty():
    global top
    if top == -1:
        return True
    else:
        return False

def popEle():
    global top
    stack.pop()
    top -= 1

def pushEle(temp):
    global top
    top += 1
    stack.append(temp)

for i in range(0, len(exp)):
    if exp[i] == '[' or exp[i] == '(' or exp[i] == '{':
        pushEle(exp[i])
    
    elif exp[i] == ')':
        if isEmpty():
            print("Unbalanced expresson..")
            break
        else:
            if stack[top] == '(':
                popEle()

    elif exp[i] == '}':
        if isEmpty():
            print("Unbalanced expresson..")
            break
        else:
            if stack[top] == '{':
                popEle()
            else:
                print("Unbalanced expresson..")
                break

    elif exp[i] == ']':
        if isEmpty():
            print("Unbalanced expresson..")
            break
        else:
            if stack[top] == '[':
                popEle()
            else:
                print("Unbalanced expresson..")
                break
else:
    if isEmpty():
        print("Balanced expression..")
    else:
        print("Unbalanced expression..")
