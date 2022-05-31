top = -1
stack_list = []
lenght = 4
exit = 0
def isEmpty():
    global top
    if top == -1:
        return True
    else:
        return False

def isFulll():
    global top
    if top == lenght:
        return False
    else:
        return True

def push():
    global top, exit
    if isFulll():
        top += 1
        ele = int(input("Enter Element: "))
        stack_list.append(ele)
    else:
        print("Stack Overflow!")
        print("\nYour Stack: ")
        for i in range(top, -1, -1):
            print(stack_list[i])
        exit = 4

def pop():
    global top, exit
    if isEmpty():
        print("Stack Underflow!!")
        exit = 4
    else:
        top -= 1
        
def showStack():
    global top
    print("Your Stack: ")
    for i in range(top, -1, -1):
        print(stack_list[i])

while exit != 4:
    print('\n1. Insert new Element: \n2. Delete Last in element\n3. View your Stack\n4. Exit form Programm')
    exit = int(input("\nEnter your choice: "))
    if exit == 1:
        push()
    elif exit == 2:
        pop()
    elif exit == 3:
        showStack()