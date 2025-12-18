S = input()
minimum = 0
past = None
if S[0] == 'o':
    S = 'i' + S
    minimum += 1
if S[-1] == 'i':
    S += 'o'
    minimum += 1

for i in range(len(S)):
    if S[i] == past:
        minimum += 1
    past = S[i]

print(minimum)