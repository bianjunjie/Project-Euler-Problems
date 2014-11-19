""" Algorithm
Broute force: randomly select 5 numbers from 1-10, put it randomly in the centeral pentagon
The first number may be put fixed, while other numbers can be put randomly, forming C(10,5)*4! kinds
For other numbers, each 3-number-edge's sum = (55+(sum of centeral 5 numbers))/5
"""


import itertools
import commonFunc as cf

N = 5
def magic_string(centeral, corner):
    global N 
    start = corner.index(min(corner))
    s = ''
    for i in range(start, start+len(centeral)):
        k = i%N
        s += str(corner[k]) + str(centeral[k]) + str(centeral[(k+1)%N])
    return s


@cf.timeit    # for time measure
def main():
    global N 
    centeral = [0] * N
    corner   = [0] * N
    numbers = range(1,11);
    ans = []
    for c in itertools.combinations(numbers, N):
        choice = list(c)
        if sum(choice) % N: continue
        total = 11 + sum(choice)/N
        centeral[0] = choice[0]
        for p in itertools.permutations(choice[1:]):
            centeral[1:] = p[:]
            for i in range(N):
                corner[i] = total - centeral[i] - centeral[(i+1)%N]

            if set(corner + centeral) != set(range(1,11)): continue
            s = magic_string(centeral, corner)
            if len(s) != 16: continue
            ans.append(s)
    print max(ans)

main()
