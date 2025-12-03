N = int(input())
A_list = list(map(int,input().split()))
answer = 0
for x in range(N+1):
    count = sum(1 for value in A_list if value >= x)
    if count >= x:
        answer = x
print(answer)