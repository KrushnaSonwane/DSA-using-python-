top = -1
exp = input("Enter your expression: ")
stack = []

def isEmpty():
    global top
    if top == -1:
        return True
    else:
        return False

def pop():
    global top
    if isEmpty():
        return True
    else:
        return False

def push(ele):
    global top
    
    stack.append(ele)

for i in range(0, len(exp)):
    if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
        top = top + 1
        push(exp[i])
    elif exp[i] == ')' or exp[i] == '}' or exp[i] == ']':
        if pop():
            flag = 1
            break
        else:
            if stack[top] == '(':
                if exp[i] == ')':
                    stack.pop(top)
                    top = top - 1
                else:
                    break

            elif stack[top] == '{':
                if exp[i] == '}':
                    stack.pop(top)
                    top = top - 1
                else:
                    break

            elif stack[top] == '[':
                if exp[i] == ']':
                    stack.pop(top)
                    top = top - 1
                else:
                    break
            else:
                break

if isEmpty():
    print("Balanced expression..")
else:
    print("UnBalanced expression..!")