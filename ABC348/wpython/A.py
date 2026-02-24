N = int(input())
idx = 1
output = ""
for _ in range(N):
    if idx == 3:
        output += "x"
        idx = 1
    else:
        output += "o"
        idx += 1
print(output)