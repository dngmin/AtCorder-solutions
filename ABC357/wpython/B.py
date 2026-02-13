S = input()
up = 0
low = 0
for i in range(len(S)):
    if S[i].isupper():
        up += 1
    else:
        low += 1
    if up > len(S)//2:
        print(S.upper())
        break
    elif low > len(S)//2:
        print(S.lower())
        break