N, M, K = map(int,input().split())

solved = dict()
winner = list()
for i in range(0,K):
    A,B = map(int,input().split())
    if A in solved:
        solved[A].append(B)
    else:
        solved[A] = [B]
    if len(solved[A]) == M:
        winner.append(A)

print(" ".join(map(str,winner)))