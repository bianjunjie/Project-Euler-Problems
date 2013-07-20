import math

#
#\frac{c}{sqrt(a) - b}
def getnext(a,b,c):
    real =int( c/(math.sqrt(a)-b) )
    new_a = a
    new_b = (b*c-real*(a-b*b))/c *-1
    new_c = (a-b*b)/c
    return real,new_a,new_b,new_c

def expand(n):
    r=[]
    real = int(math.sqrt(n))
    r.append(real)
    a = n
    b = real
    c = 1
    loop = [[a,b,c]]
    while True:
        real,new_a,new_b,new_c = getnext(a,b,c)
        r.append(real)
        loop.append([new_a,new_b,new_c])
        found = False
        for val in loop[:-1]:
            if new_a==val[0] and new_b==val[1] and new_c==val[2]:
                found = True
                break
        if found: break
        a = new_a
        b = new_b
        c = new_c
#    print r,loop
    return len(r)-1

odd = 0
for i in range(2,10000+1):
    real = int(math.sqrt(i))
    if real*real == i: continue
    if expand(i)%2==1: odd = odd+1
print odd



    

