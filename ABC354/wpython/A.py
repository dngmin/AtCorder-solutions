H = int(input())
tall = 0
i = 0
while tall <= H:
    tall += 2**i
    i += 1
print(i)