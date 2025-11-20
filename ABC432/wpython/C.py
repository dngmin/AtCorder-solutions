N, X, Y = map(int,input().split())
A_list = list(map(int,input().split()))
W_min = 0
W_max = 0

for i in range(N):
    if A_list[i]*X > W_min:
        W_min = A_list[i]*X
    if W_max == 0 or A_list[i]*Y < W_max:
        W_max = A_list[i]*Y

W = None
for candidate in range(W_max,W_min-1,-1):
    W = candidate
    for A in A_list:
        if (candidate - A*X)%(Y-X) == 0:
            continue
        else:
            W = None
            break
    if W:
        break

l_candy = 0
if W:
    for A in A_list:
        l_candy += (W - A*X)/(Y-X)
    print(int(l_candy))
else:
    print(-1)