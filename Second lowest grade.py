import sys
k = int(input())
p =[[0 for x in range(2)] for y in range(k)]
d=[]
if k<2 or k>5:
    sys.exit()
for i in range(0, k):#to get input
    for j in range(0,2):
        if j==1:
            p[i][j]=float(input())
        else:
            p[i][j]=input()
for i in range(0, k):# to sort the list in ascendng order
    for j in range(0,k-1):
            if p[i][1]<p[j][1]:
                temp=p[j]
                p[j]=p[i]
                p[i]=temp
#print(p)
for i in range(k-1):#to find the second lowest grade
    if p[i][1]==p[i+1][1]:
        count=0
    else:
        max1=p[i+1][1]
        break
#print(max1)
for i in range(0, k):#collecting all the elements matching second lowest grade
    if float(max1)==float(p[i][1]):
        d.append(p[i])

for i in range(len(d)-1):#to sort the collected elements in alphabetic order
    if p[i][0]>p[i+1][0]:
        temp=p[i+1][0]
        p[i+1][0]=p[i][0]
        p[i][0]=temp
for i in range(len(d)):#printing elements in the list
    print(d[i][0])

