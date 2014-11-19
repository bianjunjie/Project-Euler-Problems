import prime

primes = prime.myprime(10000)

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

def filter_bad(ps):
    index = [0] * len(ps)
    for i in range(len(ps)):
        print i
        for j in range(i+1, len(ps)):
            if isPair(ps[i], ps[j]):
                index[i] += 1
                print ps[j],
        print
    print index
    return index


            
def search(cur, remain):
#    print cur
    if len(cur) == 5:
        print cur, sum(cur)
        return
    if len(remain) + len(cur) < 5:
        return

    for i in range(len(remain)):
        cur.append(remain[i])
        nextRemain = []
        for r in remain[i+1:]:
            if isPair(cur[-1], r):
                nextRemain.append(r)
        search(cur, nextRemain)
        cur.pop()

            
    
cur = []
print len(primes)
#p = filter_bad(primes)
#print p
search(cur, primes[1:])
