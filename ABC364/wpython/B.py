H, W = map(int,input().split())
Si, Sj = map(int,input().split())
grid = [input() for _ in range(H)]
X = input()
i, j = Si-1, Sj-1

for way in X:
    if way == 'L':
        if j != 0 and grid[i][j-1] == '.':
            j -= 1
    elif way == 'R':
        if j != W-1 and grid[i][j+1] == '.':
            j += 1
    elif way == 'U':
        if i != 0 and grid[i-1][j] == '.':
            i -= 1
    else:
        if i != H-1 and grid[i+1][j] == '.':
            i += 1
print(i+1, j+1)