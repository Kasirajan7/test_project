def count_substring(string, sub_string):
    s=string
    v=sub_string
    k=len(v)
    count=0
    for i in range(0, (len(s)-k+1)):
        if v==s[i:(i+k)]:
            count+=1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
