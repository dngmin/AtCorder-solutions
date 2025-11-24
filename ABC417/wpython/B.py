N, M = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))

for i in B_list:
    if i in A_list:
        A_list.remove(i)
    else:
        continue

print(" ".join(map(str,A_list)) if A_list else "")