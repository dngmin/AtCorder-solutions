N, L = map(int,input().split())
A_list = list(map(int,input().split()))
output = 0
for A in A_list:
    if A >= L:
        output += 1
print(output)