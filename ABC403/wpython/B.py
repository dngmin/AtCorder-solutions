T = input()
U = input()
len_U = len(U)

T_parts = [T[0+i:len_U+i] for i in range(len(T)-len_U+1)]

for part in T_parts:
    possible = True
    for i in range(len_U):
        if part[i] != '?' and part[i] != U[i]:
            possible = False
            break
    if possible:
        break

print("Yes" if possible else "No")