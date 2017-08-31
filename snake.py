a=(0,1,2,22,4,8,6,7,8,9,10,26,12,13,14,15,16,4,18,7,29,9,22,23,24,25,26,1,28,29)
print("Your at position 1")
print("Enter the number between 1 to 6 ")
i=1
while (i<30 and i>0 ):
    n=int(input("Enter the position to move "))
    if n>0 and n<7:
        i=a[i]+n
        if i>30:
            print("Out of board")
            i=i-n
            i=a[i]
            print("Your current position is ",i)
        elif i==30:
            print ("Congrats your reach the end")
            break
        else:
            i=a[i]
            print("Your current position is ",i)
    else:
        print("Enter valid number to move ")
    
        
            
