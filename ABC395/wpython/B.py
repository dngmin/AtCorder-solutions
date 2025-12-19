N = int(input())
grid = [[0]*N for _ in range(N)]

for i in range(0,N):
    j = N - i
    if i <=j:
        color = "#" if i%2 == 0 else "."
        for a in range(i,j):
            for b in range(i,j):
                grid[a][b] = color
for i in range(N):
    print("".join(grid[i]))