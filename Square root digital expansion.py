from decimal import getcontext, Decimal
L=int(input())
d=int(input())
getcontext().prec = d+L
s = 0
p = pow(10, d-1)

for z in range(2, L+1):
    q = Decimal(z).sqrt()
    s += sum(int(c) for c in str(q * p)[:d]) if  q % 1 != 0 else 0
 
print (s)
