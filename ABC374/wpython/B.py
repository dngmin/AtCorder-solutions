S = input()
T = input()
varnished = False

for i in range(min([len(S),len(T)])):
    if S[i] != T[i]:
        varnished = True
        break
if varnished:
    print(i+1)
else:
    print(0 if len(S)==len(T) else min([len(S),len(T)])+1)