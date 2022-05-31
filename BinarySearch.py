a = [2, 9, 13, 24, 43, 45, 78, 90, 156]
low = 0
high = 9
f = 0
num = (int(input("Enter number which you want to search: ")))
for i in range(0,10):
    mid = int((high+low)/2)
    if(a[mid] > num):
        high = mid
    if(a[mid] < num):
        low = mid
    if(a[mid] == num):
        f = 1
        break
if(f==0):
    print("Sorry, Element not foun!!")
else:
    print("Element found at: ",mid+1)


# ********************User Inputs*************************


n = int(input("Enter the size of arry: "))
a = []
print("Plase Enter sorted list : ")
for i in range(0,n):
    ele = int(input())
    a.append(ele)
low = 0
high = n
f  = 0
num = (int(input("Enter number which you want to search: ")))
for i in range(0,n-1):
    mid = int((high+low)/2)
    if(a[mid] > num):
        high = mid
    if(a[mid] < num):
        low = mid
    if(a[mid] == num):
        f = 1
        print("Element found at: ",mid+1)
        break
if(f==0):
    print("Sorry, Element not foun!!")