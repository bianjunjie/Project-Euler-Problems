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


    
for i in xrange(len(primes)):
    
