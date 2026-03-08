N, X = map(int,input().split())
A_list = list(map(int,input().split()))
for A in A_list:
    if A < X:
        X = A
        print(1)
    else:
        print(0)