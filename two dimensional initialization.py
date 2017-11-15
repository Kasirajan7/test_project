count=0
w=5
h =5
Catrix = [[0 for x in range(w)] for y in range(h)]
print(Catrix)
for i in range(h):
    for j in range(w):
        #print(i,j)
        Catrix[i][j]=count
        count+=1
        #print()

for i in range(h):
    for j in range(w):
        #print(i,j)
        print(Catrix[i][j],end=" ")
    print()

