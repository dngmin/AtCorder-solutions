N, M = map(int,input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

for a in range(N-M+1):
    for b in range(N-M+1):
        matching = True
        for i in  range(M):
            if S[a+i][b:b+M] != T[i]:
                matching = False
                break
        if matching:
            print(a+1,b+1)
            exit()