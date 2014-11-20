'''
Algorithm for generating *ALL* pythagorean triple
select m,n, m>n, m-n odd, and with m and n coprime
a = m*m - n*n
b = 2*m*n
c = m*m + n*n
then (ka,kb,kc) is pythagorean triple for all k>=1

Using this method, every pythagorean triple will be generated
and generated only once
'''

import commonFunc as cf
import math

@cf.timeit
def main():
    # a + b + c = 2m(m+n) <= maxL
    # => n <= 1/2 sqrt(maxL) 
    # => m <= sqrt(1/2 maxL) 
    maxL = 1500000
    maxN = int(math.sqrt(maxL) * 0.5)
    maxM = int(math.sqrt(0.5*maxL))
    l = [0] *(maxL+1)
    for n in range(1, maxN+1):
        for m in range(n+1, maxM, 2):
            if cf.GCD(m,n) != 1: continue
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            s = a + b + c

            while s <= maxL:
                l[s] += 1
                s += (a+b+c)
    return l

l = main()
print sum([i for i in l if i==1])
