a = []
f=0
n = int(input("Enter the size of array : "))
print("Enter elements :")
for i in range(0, n):
    ele = int(input())
    a.append(ele)
num = int(input("Enter element that you want to search : "))
for i in range(0, n):
    if(num == a[i]):
        f = i+1
        break
if(f==0):
    print("Sorry, Elment not found!!")
else:
    print("Elment found at: ",f)