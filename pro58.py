import prime

prime_list = prime.myprime(1000000)
prime_dict = {}
for ps in prime_list:
    prime_dict[ps]=1

def isprime(n):
    if prime_dict.has_key(n):
        return True
    for ps in prime_list:
        if ps*ps>n: return True
        if n%ps==0: return False
    return True

side = 3
total_diag= 5
p=[3,5,7]

ratio = len(p)*1.0/total_diag
while ratio > 0.1:
    side = side + 2
    total_diag += 4
    p1 = side*side - side +1
    if isprime(p1): p.append(p1)

    p1 = p1 - side +1
    if isprime(p1): p.append(p1)

    p1 = p1 - side +1
    if isprime(p1): p.append(p1)
    ratio = len(p)*1.0/total_diag
    if ratio <0.1: break
print side,ratio

