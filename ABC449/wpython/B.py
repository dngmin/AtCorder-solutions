H, W, Q = map(int,input().split())
for _ in range(Q):
    t, n = map(int,input().split())
    if t == 1:
        print(W*n)
        H -= n
    else:
        print(H*n)
        W -=n