H, W, N = map(int,input().split())
A_grid = []
for _ in range(H):
    row = list(map(int,input().split()))
    A_grid.append(row)

B_list = [int(input()) for _ in range(N)]

maximum = 0
for i in range(H):
    count = 0
    for B in B_list:
        if B in A_grid[i]:
            count +=1
    if count > maximum:
        maximum = count
print(maximum)