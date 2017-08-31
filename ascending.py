n=int(input ("Enter how numbers to be inputed"))
print("Enter the numbers")
a=[int(input()) for i in range(n)]
count1=0
count=0
j=1
for i in range(n):
    for j in range(n-1):
        if a[i]<a[j]:
            count+=1
        else:
            break
for i in range(n):
    for j in range(n-1):
        if a[i]>a[j]:
            count1+=1
        else:
            break
k=0
d=0
for i in range(n):
    k=k+d
    d+=1
if count==k:
    print("Descending")
elif count1==k:
    print("Ascending")
else:
    print("Unsorted list")
