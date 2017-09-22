n=int(input())
#print(n)
c=[int(input())for i in range(n)]
#print(c)
for i in range(n):
    j=1
    sum=0
    d=-1
    while sum>d:
        sum=sum+j
        #print(sum)
        a=sum
        a=a//2
        b=sum
        count=0
        #print(1)
        for k in range(1,a):
            if b%k==0:
                count+=1
            if count>=c[i]:
                #print(sum)
                break
        if count>=c[i]:
            print(sum)
            break
        j+=1
        d=0
