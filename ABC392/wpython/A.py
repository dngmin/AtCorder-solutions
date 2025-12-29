A_list = list(map(int,input().split()))
A_list.sort()
print("Yes" if A_list[0] * A_list[1] == A_list[2] else "No")