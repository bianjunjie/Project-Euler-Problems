chain = [-1] * 4000000
fact = [1] * 10
for i in range(1, 10):
    fact[i] = i * fact[i-1]

def sum_of_fact(n):
    s = 0
    while n:
        s += fact[n%10]
        n /= 10
    return s



def solve(n):
    global chain
    if chain[n] != -1: return chain[n]
    
    c = [n]
    while True:
        next_n = sum_of_fact(n)
        if chain[next_n] != -1:
            break
        if next_n not in c:
            c.append(next_n)
            n = next_n
        else:
            break
    if chain[next_n]!=-1:
        for (i,val) in enumerate(c):
            chain[val] = len(c) - i + chain[next_n]
    else:
        for (i, val) in enumerate(c):
            if chain[val] == -1:
                chain[val] = len(c) - i

def print_chain(n):
    c = [n]
    while True:
        next_n = sum_of_fact(n)
        if next_n not in c:
            c.append(next_n)
            n = next_n
        else:
            break
    return c


#c = print_chain(1479)
#print c, len(c)

for i in range(1000000):
    solve(i)

m = max(chain[:1000000])
print m

s = [i for (i,c) in enumerate(chain[:1000000]) if c == m]
print s
print len(s)


