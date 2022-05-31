infix = input("Enter infix expression: ")
stack = []
priority_values = [1, 2, 3]
top = -1
postfix = ''

def isEmpty():
    global top
    if top == -1:
        return True
    else:
        return False

def pushEle(ele):
    global top
    top += 1
    stack.append(ele)

def popEle(ele):
    global top
    stack.pop(ele)
    top -= 1

for i in range(0, len(infix)):
    if infix[i] == '+' or infix[i] == '-':
        if isEmpty():
            pushEle(infix[i])
        else:
            if stack[top] == '+' or stack[top] == '-':
                pushEle(infix[i])
            else:
                
