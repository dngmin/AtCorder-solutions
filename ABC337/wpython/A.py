N = int(input())
t, a = 0, 0
for _ in range(N):
    X, Y = map(int,input().split())
    t += X
    a += Y
print("Draw" if t == a else "Takahashi" if t > a else "Aoki")