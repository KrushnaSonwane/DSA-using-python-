n = int(input("Enter the size of arry: "))
a = []
b = []
for i in range(0,n):
    num = int(input())
    a.append(num)
b = a
location = int(input("Enter Location, that number you want to delete: "))
for i in range(0,n-1):
    if(location-1==i):
        b[i] = a[i+1]
    if(location-1<i):
        b[i] = a[i+1]
for i in range(0,n-1):
    print(b[i])
