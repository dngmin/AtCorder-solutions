N, M, P = map(int,input().split())
if N < M:
    print(0)
else:
    print(1+(N-M)//P)