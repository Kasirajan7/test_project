import sys
if __name__ == '__main__':
    s = input()
    i=0
    j=0
    a,b=0,0
    for x in s:
        if x.isalpha():
            b+=1
        if x.isdigit():
            a+=1
        if x.islower():
            i+=1
        if x.isupper():
            j+=1
    if b>0 or a>0 :
            print("True")
    else:
            print("False")
    if b>0:
            print("True")
    else:
            print("False")
    if a>0:
            print("True")
    else:
            print("False")

    if i>0:
            print("True")
    else:
            print("False")
    if j>0:
            print("True")
    else:
            print("False")
