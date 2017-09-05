a=(0,1,2,22,4,8,6,7,8,9,10,26,12,13,14,15,16,4,18,7,29,9,22,23,24,25,26,1,28,29,30)
#print("Your at position 1")
#print("Enter the number between 1 to 6 ")
i=1
p=[0,1,2,3,4,5]
count=0
k=0
while (i<30 and i>0 ):
    n=1
    #n=int(input("Enter the position to move "))
    while n<7 :
        l=a[i]
        i=a[i]+n
        #print(i)
        if i>30:
            #print("Out of board")
            i=i-n
            i=a[i]
            #print("Your current position is ",i)
        p[k]=a[i]
        n+=1
        i=l
        k+=1
    k=0
    p.sort()
    i=p[5]
    #print(p[5])
    if i==30:
            #print ("Congrats your reach the end")
            break
    else:
            i=a[i]
            count+=1
            #print("Your current position is ",i)
print(count+1)
    
        
