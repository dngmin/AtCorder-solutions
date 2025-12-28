N, M = map(int,input().split())
S = list(map(int,input()))
T = list(map(int,input()))

minimun = len(T)*10

for starting in range(N-M+1):
    count = 0
    for i in range(len(T)):
        if S[starting+i] > T[i]:
            count += S[starting+i] - T[i]
        elif S[starting+i] < T[i]:
            count += 10 + S[starting+i] - T[i]
    if count < minimun:
        minimun = count
    if count == 0:
        break
print(minimun)