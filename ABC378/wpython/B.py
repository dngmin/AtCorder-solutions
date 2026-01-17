N = int(input())
qr = [list(map(int,input().split())) for _ in range(N)]
Q = int(input())
output = []
for _ in range(Q):
    t, d = map(int,input().split())
    q, r = qr[t-1]
    day = r
    if d <= r :
        day = r
    elif r < d <= q:
        day = q + r
    else:
        day = (d//q) * q + r
        day += q if day < d else 0

    output.append(day)

for day in output:
    print(day)