N, K = map(int,input().split())
output = 0
for n in range(1,N+1):
    sum = 0
    n = str(n)
    for digit in n:
        sum += int(digit)
        if sum > K:
            break
    if sum == K:
        output += 1
print(output)