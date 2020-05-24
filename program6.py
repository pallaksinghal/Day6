a=0
n = int(input("Enter length: "))
arr=[]
for i in range(n):
    d=int(input("Enter element : "))
    arr.append(d)
for i in range(0,n-1):
    if arr[i]>arr[i+1]:
        a=1
        break
if a==1:
    print("Your array",arr,"is not sorted.")
else:
    print("Your array", arr, "is sorted.")
