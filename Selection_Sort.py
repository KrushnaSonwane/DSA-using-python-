n = int(input("Enter size of array: "))
a = []
for i in range(0,n):
    ele = int(input())
    a.append(ele)
for i in range(0,n,1):
    for j in range(i+1,n,1):
        if(a[i]>a[j]):
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print("Sorted Array: ")
for i in range(0,n):
    print(a[i])