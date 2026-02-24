N = int(input())
xy = []
for _ in range(N):
    x, y = map(int,input().split())
    xy.append([x,y])
output = []
for i in range(N):
    max_distance = [0,0]
    for j in range(N):
        distance = (xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2
        if distance > max_distance[1]:
            max_distance = [j+1, distance]
    output.append(max_distance[0])
for o in output:
    print(o)