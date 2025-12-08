N = int(input())
grid_S = [input() for _ in range(N)]
grid_T = [input() for _ in range(N)]
count = 0

# rotate 0
for i in range(N):
    for j in range(N):
        if grid_S[i][j] != grid_T[i][j]:
            count+=1
minimum = count

# rotate 1
count = 1
for i in range(N):
    for j in range(N):
        if grid_S[N-j-1][i] != grid_T[i][j]:
            count+=1
if count < minimum:
    minimum = count

# rotate 2
count = 2
for i in range(N):
    for j in range(N):
        if grid_S[N-i-1][N-j-1] != grid_T[i][j]:
            count+=1
if count < minimum:
    minimum = count

# rotate 3
count = 3
for i in range(N):
    for j in range(N):
        if grid_S[j][N-i-1] != grid_T[i][j]:
            count+=1
if count < minimum:
    minimum = count
print(minimum)