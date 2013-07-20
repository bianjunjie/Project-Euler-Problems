def poly():
    P={}
    start={}
    end={}
    P[3]=[]
    for n in range(45,141):
        P[3].append(n*(n+1)/2)
    P[4]=[]
    for n in range(32,100):
        P[4].append(n*n)
    P[5]=[]
    for n in range(26,82):
        P[5].append(n*(3*n-1)/2)
    P[6]=[]
    for n in range(23,71):
        P[6].append(n*(2*n-1))

    P[7]=[]
    for n in range(21,64):
        P[7].append(n*(5*n-3)/2)
    P[8]=[]
    for n in range(19,59):
        P[8].append(n*(3*n-2))

    start[3]=45; start[4]=32; start[5]=26; start[6]=23; start[7]=21; start[8]=19;
    end[3]=141;  end[4]=100;  end[5]=82;   end[6]=71;   end[7]=64;   end[8]=59;
    return P,start,end

P,start,end=poly()


#
#example: [1424,2417,1722], 2276   True
def match(cur, val):
    last = cur[-1]
    for c in cur: 
        if c == val: return False
    if last%100 == val/100: return True
    return False

def search(cur, N):
    if len(N)==6:
        if cur[-1]%100 == cur[0]/100:
            print cur, sum(cur),N
        return
    for i in range(3,8+1):
        if i in N: continue
        for val in P[i]:
            if match(cur, val):
                search(cur+[val], N+[i])
        
        
for val in P[8]:
    tail = val%100
    if tail<10: continue
    search([val], [8])

