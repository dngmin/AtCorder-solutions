N, X, Y, Z = map(int,input().split())
print("Yes" if min(X,Y) < Z < max(X,Y) else "No")