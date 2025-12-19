N = int(input())
A_list = list(map(int,input().split()))
increasing = True
for i in range(N-1):
    if A_list[i] >= A_list[i+1]:
        increasing = False
        break
print("Yes" if increasing else "No")