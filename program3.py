a=1
n = int(input("Enter length: "))
arr = []
for i in range(n):
    d = int(input("Enter element : "))
    arr.append(d)
for i in range(n):
    if a in arr:
        a+=1
    else:
        break
print("Smallest missing number: ",a)
