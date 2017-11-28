
def relation(length):
    s=['f','l','a','m','e','s']
    s1=6
    while s1>1:
        for i in range(length-1):
            s.insert(0,s.pop())
        #print(s.pop())
        s1=len(s)
    final=s.pop()
    if final=='f':
        print("Friends")
    elif final=='l':
        print("Love")
    elif final=='a':
        print("Affection")
    elif final=='m':
        print("Marriage")
    elif final=='e':
        print("Enemy")
    else:
        print("Sister")


str1=input("Enter the Male Name: ").strip()
str2=input("Enter the Female Name: ").strip()
str1=str1.replace(" ","")
str2=str2.replace(" ","")
str1=list(str1.lower())
str2=list(str2.lower())
count=0
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i]==str2[j]:
            str2[j]=9
            count+=1
            break
count=count*2
length=len(str1)+len(str2)-count
relation(length)
