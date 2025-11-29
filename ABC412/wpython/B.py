S = input()
T = input()
T_set = set()
precondition = True
for i in range(len(T)):
    T_set.add(T[i])

for j in range(len(S)):
    if j == 0:
        continue
    if S[j].isupper() and not S[j-1] in T_set:
        precondition = False
        break
if precondition:
    print("Yes")
else:
    print("No")