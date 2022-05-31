queue_list = []
rear = -1
lenght = 4
front = 0
choice = 0

def isEmpty():
    global rear, front
    if rear == -1 or front > rear:
        return True
    else:
        return False

def isFull():
    global front, rear
    if rear >= lenght:
        return True
    else:
        return False
    
def push():
    global rear, front, choice
    if isFull():
        print("\nQueue Overflow..!!")
        choice = 4
    else:
        print("Enter element: ")
        rear += 1
        ele = int(input())
        queue_list.append(ele)

def pop():
    global front, rear, choice
    if isEmpty():
        print("\nQueue Underflow..!!")
        choice = 4
    else:
        queue_list[front] = None
        front += 1

def show():
    global front, rear
    print("\nYour Queue: ", end="")
    for i in range(front, rear+1):
        print(queue_list[i], end=" ")
    else:
        print()

while choice != 4:
    choice = int(input("1.Inserr\n2.Delete\n3.Show\n4.Exit from Queue\nEnter your Choice: "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        show()
    elif choice == 4:
        break
    else:
        print("OOPS..... Please Enter valid choice..!!")