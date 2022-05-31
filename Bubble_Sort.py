n = int(input("Enter size of array: "))
a = []
for i in range(0,n):
    ele = int(input())
    a.append(ele)
for i in range(0,n):
    for j in range(0,n-1):
        if(a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print("sorted List: ")
for j in range(0,n):
    print(a[j])