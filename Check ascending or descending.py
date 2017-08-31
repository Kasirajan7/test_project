import copy
n=int(input ("Enter how numbers to be inputed"))
print("Enter the numbers")
a=[int(input()) for i in range(n)]
b=copy.copy(a)
b.sort()
c=copy.copy(a)
c=(sorted(a,key=int,reverse=True))
if b==a:
    print("Ascending order")    
elif c==a:
    print("Descending order")
else:
    print("Unsorted list")
