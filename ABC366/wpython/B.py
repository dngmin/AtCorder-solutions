N = int(input())
S_list = list()
T_list = list()
M = 0
for _ in range(N):
    S = input()
    S_list.append(S)
    if len(S) > M:
        M = len(S)

for i in range(N):
    if len(S_list[i]) < M:
        S_list[i] += "*" * (M - len(S_list[i]))

for i in range(M):
    T = ""
    for j in range(N):
        T += S_list[N-j-1][i]
    if T[-1] == "*":
        for k in range(1,len(T)+1):
            if T[-k] != "*":
                break
        T = T[:-k+1]

    T_list.append(T)

for T in T_list:
    print(T)