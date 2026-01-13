N, D = map(int,input().split())
S = input()
empty = 0
for s in S:
    if s == ".":
        empty += 1
print(empty+D)