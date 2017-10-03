n=input()
l=[]
j=0
k=list(n)
length=len(n)
for i in range(0,length):
    if k[i].isalpha():
        l.append(k[i])
        #print(l)
for i in range (length-1,-1,-1):
    if k[i].isalpha():
        k[i]=l[j]
        #print(l[j])
        j+=1
print(''.join(k))
