N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
element = 1

for i in range(1,N+1):
    element = A[element-1][i-1] if element >= i else A[i-1][element-1]
print(element)