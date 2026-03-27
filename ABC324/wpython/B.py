N = int(input())
while N%2 == 0:
    N //= 2
for y in range(N):
    if 3**y == N:
        print("Yes")
        break
    if 3**y > N:
        print("No")
        break