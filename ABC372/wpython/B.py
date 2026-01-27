M = int(input())
A = []
for _ in range(20):
    for i in range(10,-1,-1):
        if 3**i <= M:
            break
    M -= 3**i
    A.append(i)
    if M == 0:
        break
print(len(A))
print(" ".join(map(str,A)))