import prime

prime_list = prime.myprime(1000000)
prime_dict = {}
for val in prime_list:
    prime_dict[val] = True

def expand_to_primes(n):
    d = {}
    i = 0
    while i<len(prime_list):
        if n% prime_list[i]==0:
            d[prime_list[i]] = d.get(prime_list[i],0)+1
            n /= prime_list[i]
        else:
            i=i+1
        if n==1: break
    return d

best_n = -1
best_ans=-1
N = 1000000+1
ans_dict={}

for val in prime_list:
    ans_dict[val] = val -1

for val in prime_list:
    cur = val*val
    k = 2
    while cur<N:
        ans_dict[cur] = val**(k-1)*(val-1)
        k = k+1
        cur = cur*val
for i in range(2,N):
    if i%10000==0: print i
    if ans_dict.has_key(i): 
        continue
    for val in prime_list:
        if i%val==0:
            break
    k = 1
    while i%(val**k)==0:
        k=k+1
    k = k - 1
    ans_dict[i] = ans_dict[val**k]*ans_dict[i/(val**k)]

for i in range(2,11): print i,ans_dict[i]
for i in range(2,N):
    ans = i*1.0/ans_dict[i]
    if ans > best_ans:
        best_ans = ans
        best_n = i
print best_n, best_ans
