N = int(input())
square = []

for _ in range(N):
    square.append([0]*N)

r, c, k = 0, int((N-1)/2), 1
square[r][c] = k

for _ in range(N**2 - 1):
    k += 1
    if square[(r-1)%N][(c+1)%N] == 0:
        square[(r-1)%N][(c+1)%N] = k
        r, c = (r-1)%N, (c+1)%N
    else:
        square[(r+1)%N][c] = k
        r, c = (r+1)%N, c

for i in range(N):
    print(" ".join(map(str,square[i])))