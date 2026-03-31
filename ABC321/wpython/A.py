N = int(input())
pre = -1
while N > 0:
    cur = N % 10
    if cur <= pre:
        print("No")
        break
    N //= 10
    pre = cur
else:
    print("Yes")