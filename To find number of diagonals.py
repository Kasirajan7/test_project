n=int(input ("Enter the sides "))
k=0
d=0
for i in range(n):
    k=k+d
    d+=1
d=k-n
if d==0:
    print("No diagonal")
else:
    print("It has ",d," Diagonal")
