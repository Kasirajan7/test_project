n=int(input())
sum1=0
sum2=0
for i in range(10,n):
    b=i
    sum1=0
    while b>0:
        a=b%10
        sum=1
        for j in range(1,a+1):
            sum=sum*j
        sum1=sum1+sum
        b=b//10
    c=sum1/i
    d=sum1//i
    if c==d:
        sum2=sum2+i
print(sum2)
            
            
    
