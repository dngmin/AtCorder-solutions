N, S, M, L = map(int,input().split())
minimum = 10**6
for a in range(10):
    for b in range(14):
        for c in range(18):
            if 12*a + 8*b + 6*c < N:
                continue
            minimum = a*L + b*M + c*S if a*L + b*M + c*S < minimum else minimum
print(minimum)