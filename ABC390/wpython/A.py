A_list = list(map(int,input().split()))
check = [1,2,3,4,5]
for i in range(5):
    check[i] -= A_list[i]
print("Yes" if check.count(0) == 3 and check.count(1) == check.count(-1) == 1 else "No")