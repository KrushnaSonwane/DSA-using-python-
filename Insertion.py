

# ***********Using Insert function(in-build)************

a=[]
n = int(input("Enter size of array: "))
for i in range(0, n):
    ele = int(input())
    a.append(ele)
loc = int(input("Enter location : "))
num = int(input("Enter new numbner : "))
a.insert(loc, num)
print(a)


# *******************Using Loop*****************


a = []
b = []
n = int(input("Enter the size of array : "))
print("Enter elements :")
for i in range(1, n+1):
    ele = int(input())
    a.append(ele)
location = int(input("Enter the location : "))
num = int(input("Enter new elemnet to add : "))
for i in range(0, n+1):
    if(location-1 > i):
        b.append(a[i])
    if(location-1 == i):
        b.append(num)
    if(location-1 < i):
        b.append(a[i-1])
for i in range(0, n+1):
    print(b[i])