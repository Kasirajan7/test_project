k = int(input())
p =[[0 for x in range(4)] for y in range(k)]
for i in range(0, k):
    str1 =input()
    p[i] = str1.split()
name=input()
for i in range(0, k):#
    if name==p[i][0]:
        avg=(float(p[i][1])+float(p[i][2])+float(p[i][3]))/3
        print("%.2f" % avg)
        #print(avg)
        #print(float(p[i][1]))

