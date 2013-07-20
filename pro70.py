
import prime

N = int(1e7)
prime_list = prime.myprime(N)
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

def is_permu(m, n):
    m_str = ''.join(sorted(str(m)))
    n_str = ''.join(sorted(str(n)))
    if m_str == n_str: return True
    return False
    
best_n = -1
best_ans=-1
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

best_n = 1e10
best_ans = 1e10
for i in range(2,N):
    if is_permu(i, ans_dict[i]):
        ans = i*1.0/ans_dict[i]
        if ans < best_ans:
            best_ans = ans
            best_n = i

print best_n, best_ans



