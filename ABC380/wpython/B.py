S = input()
A_list = list()
A = 0
for s in S:
    if s == "|":
        A_list.append(A)
        A = 0
    else:
        A += 1
print(" ".join(map(str,A_list[1:])))