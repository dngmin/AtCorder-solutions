N, M = map(int,input().split())
A_list = list(map(int,input().split()))
X_list = list(range(1,N+1))
A_list.sort(reverse=True)

for A in A_list:
    X_list.pop(A-1)
    
print(len(X_list))
print(" ".join(map(str,X_list)))