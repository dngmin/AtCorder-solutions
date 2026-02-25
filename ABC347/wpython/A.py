N, K = map(int,input().split())
A_list = list(map(int,input().split()))
output = list()
for A in A_list:
    if A%K == 0:
        output.append(str(A//K))
print(" ".join(output))