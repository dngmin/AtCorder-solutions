A_list = list(map(int,input().split()))
A_set = set(A_list)
more_3 = 0
more_2 = 0
for A in A_set:
    if A_list.count(A) >= 3:
        more_3 += 1
    elif A_list.count(A) >= 2:
        more_2 += 1
print("Yes" if more_3 == 2 or (more_3 == 1 and more_2 >= 1) else "No")