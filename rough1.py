def int_to_en(num):
    d = { 0 : 'Zero', 1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five',
          6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine', 10 : 'Ten',
          11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen',
          15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen',
          19 : 'Nineteen', 20 : 'Twenty',
          30 : 'Thirty', 40 : 'Forty', 50 : 'Fifty', 60 : 'Sixty',
          70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000
    assert(0<=num)
    if num<20:
        return d[num]
    if num<100:
        if num%10==0:
            return d[num]
        else:
            return d[num//10*10]+" "+d[num%10]
    if num<k:
        if num%100==0:
            return d[num//100]+" Hundred "
        else:
            return d[num//100]+" Hundred "+int_to_en(num%100)
    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' Thousand '
        else: return int_to_en(num // k) + ' Thousand ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' Million '
        else: return int_to_en(num // m) + ' Million ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' Billion '
        else: return int_to_en(num // b) + ' Billion ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' Trillion '
    else: return int_to_en(num // t) + ' Trillion ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))
n=int(input("Test case"))    
c=[int(input("enter number")) for i in range(n)]
for i in range(n):
    num=c[i]
    print(int_to_en(num))

