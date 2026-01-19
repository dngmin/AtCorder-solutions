row = set()
column = set()

for i in range(8):
    S = input()
    for j in range(8):
        if S[j] == "#":
            row.add(i)
            column.add(j)
print((8-len(row))*(8-len(column)))