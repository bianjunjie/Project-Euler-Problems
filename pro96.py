def get_poss(grid, i, j):
    l={}
    for m in range(1,10): l[m] = True
    for m in range(9):
        if m!=i: l[grid[m][j]]=False
        if m!=j: l[grid[i][m]]=False
    for m in range(i/3*3,i/3*3+3):
        for n in range(j/3*3,j/3*3+3):
            if m==i and n==j: continue
            l[grid[m][n]]=False
    r=[]
    for k in l.keys():
        if l[k]: r.append(k)
    return r
        
result = 0
def solve(grid, i, j):
    global result
    if i==9: 
        print 'After:',grid
        result += grid[0][0]*100+grid[0][1]*10+grid[0][2]
        return
    if j==9: 
        solve(grid,i+1,0)
        return
    if grid[i][j]!=0: 
        solve(grid, i,j+1)
        return
    poss_nums = get_poss(grid, i, j)
    if len(poss_nums)==0: return
    
    for val in poss_nums:
        grid[i][j]=val
        solve(grid,i,j+1)
        grid[i][j]=0

grid=[]
row=0
for line in open('sudoku.txt'):
    if line.startswith('Grid'):
        grid=[]
        row=0
    else:
        l = []
        for ch in line.strip():
            l.append(ord(ch)-ord('0'))
        grid.append(l)
        row = row+1
        if row==9: 
            solve(grid,0,0)


print result


        
    
