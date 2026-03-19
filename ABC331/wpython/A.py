M, D = map(int,input().split())
y, m, d = map(int,input().split())
if d == D:
    if m == M:
        y += 1
        m = 1
    else:
        m += 1
    d = 1
else:
    d += 1
print(y,m,d)