a=input("String: ")
a=list(a)

b=[]
while len(a)>0:
    temp=a.pop(0)
    for i in range(len(a)):
        c=a.pop(0)
        if temp>c:
            a.append(c)
        else:
            a.append(temp)
            temp=c
    b.append(temp)
    
print(b)
