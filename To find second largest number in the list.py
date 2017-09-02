if __name__ == '__main__':
    n = int(input())
    z= list(map(int, input().split()))
    #print(int(z[0]))
    k=[]
    k=sorted(z,key=int,reverse=True)
    print(k)
    l=0
    j=1
    for i in range(n):   
            if k[l]==k[j]:
                    l+=1
                    j+=1
            else:
                    print(k[j])
                    break            
   
