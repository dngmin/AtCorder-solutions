N = int(input())
L_list = list(map(int,input().split()))
from_0 = 0
from_N = 0

for i in range(0,N):
    if L_list[i] == 1:
        from_0 = i+1
        break
for j in range(0,N):
    if L_list[N-1-j] == 1:
        from_N = N-j
        break
print(from_N - from_0)