N = int(input())
A_list = list(map(int,input().split()))
K = int(input())
count = 0
for A in A_list:
    if A >= K:
        count+=1

print(count)