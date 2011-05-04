import math

from datetime import datetime
'''
Find all prime numbers less or equal to n

speed:
    myprime > primes >> Prime
'''

def Prime(n):
    t1=datetime.now()
    if n<1:
        return []
    if n==2:
        return [2]
    m=int( math.sqrt(n))

    r=[2]+range(3,n,2)

    i=0
    while r[i]<=m:
        for j in r[i+1:]:
            if j%r[i]==0:
                r.remove(j)
        i=i+1;
    print "cost : ",datetime.now()-t1
    return r

def primes(n):
    t1=datetime.now()
    s=range(0,n+1)
    s[1]=0
    bottom=2
    top=n//bottom
    while (bottom*bottom<=n):
            while (bottom<=top):
                    if s[top]:
                            s[top*bottom]=0
                    top-=1
            bottom+=1
            top=n//bottom
    print "cost : ",datetime.now()-t1
    return [x for x in s if x]



def myprime(n):
    t1=datetime.now()
    s=range(0,n+1)
    s[1]=0
    bottom=2
    top=n//bottom
    while (bottom*bottom<=n):
            while (bottom<=top):
                    if s[top]:
                            s[top*bottom]=0
                    top-=1
            bottom+=1
            while s[bottom]==0:
                    bottom+=1
            top=n//bottom
    print "cost : ",datetime.now()-t1
    return [x for x in s if x]
