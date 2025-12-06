N, K = map(int,input().split())
A_list = list(map(int,input().split()))
ans = 1

for A in A_list:
    ans *= A
    if len(str(ans)) >= K+1:
        ans = 1
print(ans)