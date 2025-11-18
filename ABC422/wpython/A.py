stage = input()
i = int(stage[0])
j = int(stage[-1])

if j == 8:
    i += 1
    j = 1
else:
    j += 1

print(f"{i}-{j}")