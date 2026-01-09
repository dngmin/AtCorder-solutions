H, W, X, Y = map(int,input().split())
grid = [input() for _ in range(H)]
T = input()

x, y = X-1, Y-1
passed = [[x,y]]
houses = 0

for t in T:
    if t == "U" and grid[x-1][y] != "#":
        x = x-1
    elif t == "D" and grid[x+1][y] != "#":
        x = x+1
    elif t == "L" and grid[x][y-1] != "#":
        y = y-1
    elif t == "R" and grid[x][y+1] != "#":
        y = y+1
    else:
        continue
    passed.append([x,y])

passed = list(map(list,set(map(tuple,passed))))
for ix, iy in passed:
    if grid[ix][iy] == "@":
        houses += 1
print(x+1,y+1,houses)