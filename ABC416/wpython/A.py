N, L, R = map(int,input().split())
S = input()
print("Yes" if S[L-1:R].count('x') == 0 else "No")