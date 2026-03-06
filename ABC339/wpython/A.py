S = input()
for i in range(len(S)):
    if S[i] == '.':
        idx = i
print(S[idx+1:])