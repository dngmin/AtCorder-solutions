H, W = map(int,input().split())
grid = [input() for _ in range(H)]
check_adjacency = None
up = None
down = None
left = None
right = None

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            if i == 0:
                up = None
            else:
                up = grid[i-1][j]
            if i == H-1:
                down = None
            else:
                down = grid[i+1][j]
            if j == 0:
                left = None
            else:
                left = grid[i][j-1]
            if j == W-1:
                right = None
            else:
                right = grid[i][j+1]

            count = [up,down,left,right].count("#")
            if count != 2 and count != 4:
                print("No")
                exit()

print("Yes")
