H, W, N = map(int,input().split())
grid = [['.']*W for _ in range(H)]
loci, locj = 0, 0
dir = 0 #['n', 'e', 's', 'w']

for _ in range(N):
    if grid[loci][locj] == '.':
        dir = (dir+1)%4
        grid[loci][locj] = '#'
    else:
        dir = (dir-1)%4
        grid[loci][locj] = '.'
    
    if dir == 0:
        loci = (loci-1)%H
    elif dir == 1:
        locj = (locj+1)%W
    elif dir == 2:
        loci = (loci+1)%H
    else:
        locj = (locj-1)%W

for i in range(H):
    print("".join(grid[i]))