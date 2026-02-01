N, K = map(int, input().split())
mame = N
year = 0
while mame < K:
    year += 1
    mame += N + year
print(year)