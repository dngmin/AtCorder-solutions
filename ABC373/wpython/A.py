output = 0
for i in range(1,13):
    S = input()
    output += 1 if len(S) == i else 0
print(output)