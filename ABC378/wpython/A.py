A_list = list(map(int,input().split()))
maximum = 0

for A in set(A_list):
    if A_list.count(A) == 4:
        maximum += 2
    elif A_list.count(A) >= 2:
        maximum += 1
print(maximum)