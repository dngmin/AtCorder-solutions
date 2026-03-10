N = int(input())
output = 0
while N & 1 == 0:
    output += 1
    N >>= 1
print(output)