N, L, R = map(int,input().split())
A_list = list(map(int,input().split()))
output = list()
for A in A_list:
    output.append(L if A < L else R if A > R else A)
print(" ".join(map(str,output)))