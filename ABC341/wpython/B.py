N = int(input())
A_list = list(map(int,input().split()))
for i in range(N-1):
    S, T = map(int,input().split())
    A_list[i+1] += (A_list[i]//S) * T
print(A_list[-1])