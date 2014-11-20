from prime import *
import commonFunc as cf

@cf.timeit    
def countfraction(n):
    if n <= 1: return 0
    if n == 2: return 1
    
    result = 0
    phi = range(n+1)
    for i in range(2,n+1):
        if phi[i] == i:
            for j in range(i,n+1,i):
                phi[j] = phi[j]/ i*(i-1)
        result += phi[i]
    return result

print countfraction(1000000)
