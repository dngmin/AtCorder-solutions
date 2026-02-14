N, M = map(int,input().split())
goal = list(map(int,input().split()))

for _ in range(N):
    X_list = list(map(int,input().split()))
    for i in range(M):
        goal[i] -= X_list[i]
print("Yes" if max(goal) <= 0 else "No")