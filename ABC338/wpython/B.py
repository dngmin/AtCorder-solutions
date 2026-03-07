S = input()
output = list()
frequency = 0
for s in S:
    if S.count(s) > frequency:
        output = list(s)
        frequency = S.count(s)
    elif S.count(s) == frequency:
        output.append(s)
output.sort()
print(output[0])