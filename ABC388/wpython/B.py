N, D = map(int,input().split())
snake_info = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,D+1):
    maximum = 0
    for T,L in snake_info:
        if T*(L+i) > maximum:
            maximum = T*(L+i)
    print(maximum)