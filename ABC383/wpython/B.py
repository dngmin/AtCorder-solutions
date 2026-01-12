H, W, D = map(int,input().split())
grid = [input() for _ in range(H)]
floors = []
maximum = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == ".":
            floors.append([i,j])
for if1, jf1 in floors[:-1]:
    for if2, jf2 in floors[1:]:
        worked = 0
        for i, j in floors:
            if abs(if1-i)+abs(jf1-j) <= D or abs(if2-i)+abs(jf2-j) <= D:
                worked += 1
        if worked > maximum:
            maximum = worked
print(maximum)