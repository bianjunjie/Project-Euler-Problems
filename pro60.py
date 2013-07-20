import prime

primes = prime.myprime(100000)

primes_dict = {}
for p in primes:
    primes_dict[p] = 1

def isPrime(n):
    if primes_dict.has_key(n): return True
    for p in primes:
        if p*p>n: return True
        if n%p==0: return False;
    return True

def concate(m,n):
    return m*(10**len(str(n)))+n

def isPair(m,n):
    return isPrime(concate(m,n)) and isPrime(concate(n,m))

    
primeset={}
'''
for i in xrange(1,len(primes)):
    primeset[i]=[]
    for j in xrange(i+1, len(primes)):
        if isPair(primes[i], primes[j]): primeset[i].append(primes[j])
'''


def search(cur, total):
    if total==5:
        print cur,sum(cur)
        return
    vals = set(cur[0])
    for i in range(1,len(cur)):
        vals = vals & set(cur[i])
    for val in vals:
        search(cur+[val], total+1)


for i in xrange(1,len(primes)):
    s = search([primes[i]],1)


    
