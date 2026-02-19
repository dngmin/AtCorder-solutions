S = input()
T = input()
correctly_typed = []
idx = 0
for s in S:
    while s != T[idx]:
        idx += 1
    correctly_typed.append(idx+1)
    idx += 1
print(" ".join(map(str,correctly_typed)))