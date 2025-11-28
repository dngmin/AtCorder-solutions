N, M = map(int,input().split())
A_list = list(map(int,input().split()))
print("Yes" if sum(A_list) <= M else "No")