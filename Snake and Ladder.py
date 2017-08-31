sum1=1
print("You have to reach 30 to finish the game \n Your current position is 1 ")
while sum1<30:
    n=int(input ("Enter the number within 6 "))
    if n<=6 and n!=0:
        sum1+=n
        print("You have been moved to ",sum1)
        if sum1==3:
            sum1=22
            print("You have been lifted by the ladder to ",sum1)
        elif sum1==5:
            sum1=8
            print("You have been lifted by the ladder to ",sum1)
        elif sum1==11:
            sum1=26
            print("You have been lifted by the ladder to ",sum1)
        elif sum1==17:
            sum1=4
            print("You have been moved down by the snake to ",sum1)
        elif sum1==19:
            sum1=7
            print("You have been moved down by the snake to ",sum1)
        elif sum1==20:
            sum1=29
            print("You have been lifted by the ladder to ",sum1)
        elif sum1==21:
            sum1=9
            print("You have been moved down by the snake to ",sum1)
        elif sum1==27:
            sum1=1
            print("You have been moved down by the snake to ",sum1)
        elif sum1>30:
            print("Value out of range")
            sum1-=n
        elif sum1==30:
            print("Congrats you reach the end")
            break
    else:
        print("Enter the valid number within 6")
