N, L, R = map(int,input().split())
count = 0
for _ in range(N):
    listener = list(map(int,input().split()))
    if listener[0] <= L and listener[1] >= R:
        count+=1
print(count)