N, D = map(int,input().split())
S = input()
ate_cookies = 0
for i in range(N-1,-1,-1):
    ate_cookies += 1 if S[i] == "@" else 0
    if ate_cookies == D:
        break
print(S[:i]+"."*(N-i))