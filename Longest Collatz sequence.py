n=int(input())
c=[int(input()) for i in range(n)]
max=0
for i in range(n):
    a=c[i]
   
    if i>0 and c[i]>c[i-1]:
        for i in range(c[i-1],c[i]+1):
            j=i
            #print(j)
            count=0
            while j:
                if j%2==0:
                    while j%2==0:
                        j=j//2
                        count+=1
                else:
                    while j%2!=0:
                        j=(3*j)+1
                        count+=1
                if j==1:
                    break
            #print(i,count)
            if count>=max:
                #print(count,i)
                max=count
                k=i
        print(k)
    else:
        max=0
        for i in range(1,c[i]+1):
            j=i
            #print(j)
            count=0
            while j:
                if j%2==0:
                    while j%2==0:
                        j=j//2
                        count+=1
                else:
                    while j%2!=0:
                        j=(3*j)+1
                        count+=1
                if j==1:
                    break
            #print(i,count)
            if count>=max:
                #print(count,i)
                max=count
                k=i
        print(k)
    
