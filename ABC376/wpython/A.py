N, C = map(int,input().split())
T_list = list(map(int,input().split()))
last_candy_time = -C
candy = 0
for T in T_list:
    if last_candy_time + C <= T:
        candy += 1
        last_candy_time = T
print(candy)