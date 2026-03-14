N, S, K = map(int,input().split())
price = 0
for _ in range(N):
    P, Q = map(int,input().split())
    price += P*Q
print(price if price >= S else price + K)