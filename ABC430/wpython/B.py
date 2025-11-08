N,M = map(int,input().split())
grid = [input() for _ in range(N)]

subgrid_patterns = set()

for i in range(N-M+1):

    for j in range(N-M+1):
        temp = ''

        for k in range(M):
            temp+= grid[i+k][j:j+M]
        subgrid_patterns.add(temp)

print(len(subgrid_patterns))