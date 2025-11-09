X = int(input())
N = int(input())
W = list(map(int,input().split()))
Q = int(input())
P = [int(input()) for _ in range(Q)]
parts = list()
for i in range(N):
    parts.append(False)

for i in range(Q):
    if parts[P[i]-1] == False:
        X += W[P[i]-1]
        parts[P[i]-1] = True
    else:
        X -= W[P[i]-1]
        parts[P[i]-1] = False
    print(X)