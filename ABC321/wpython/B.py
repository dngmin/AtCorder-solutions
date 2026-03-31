N, X = map(int,input().split())
A_list = list(map(int,input().split()))
A_max = max(A_list)
A_min = min(A_list)
if X > sum(A_list) - A_min:
    print(-1)
elif X <= sum(A_list) - A_max:
    print(0)
else:
    print(X + A_max + A_min- sum(A_list))