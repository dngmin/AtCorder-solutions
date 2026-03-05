Q = int(input())
A = list()
for _ in range(Q):
    n, m = map(int,input().split())
    if n == 1:
        A.append(m)
    else:
        print(A[-m])