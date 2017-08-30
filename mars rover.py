z=input("Enter the two dimensional array").strip().split(" ")
a=[]
a = [[0 for i in range(int(z[0])+1)] for j in range(int(z[1])+1)]
j=input("Enter the position of the mars rover").strip().split(" ")
print("The current position of mars rover is" )
k=int(j[0])
l=int(j[1])
d=j[2]
print(k,l,d)
f=input("Enter the directions")
x=f.strip().split(" ")
g=len(x)
print(g)
for i in range(0,g):
    if d=="n"or d=="N":
        if x[i]=="l" or x[i]=="L":
            d="w"
            print(d)
        elif x[i]=="R" or x[i]=="r":
            d="e"
            print(d)
        elif x[i]=="m" or x[i]=="M":
            k=k-1
            print(k)
            
    elif d=="S"or d=="S":
        if x[i]=="l" or x[i]=="L":
            d="E"
            print(d)
        elif x[i]=="R" or x[i]=="r":
            d="W"
            print(d)
        elif x[i]=="m" or x[i]=="M":
            k+=1
            print(k)
            
    elif d=="E"or d=="e":
        if x[i]=="l" or x[i]=="L":
            d="N"
            print(d)
        elif x[i]=="R" or x[i]=="r":
            d="s"
            print(d)
        elif x[i]=="m" or x[i]=="M":
            l+=1
            print(l)
            
    elif d=="w"or d=="W":
        if x[i]=="l" or x[i]=="L":
            d="s"
            print(d)
        elif x[i]=="R" or x[i]=="r":
            d="n"
            print(d)    
        elif x[i]=="m" or x[i]=="M":
            l-=1
            print(l)
if k in range(int(z[0]))and l in range(int(z[1])):
    print("Mars rover current position is")
    print(k,l,d)
else:
    print("Invalid points")
        
