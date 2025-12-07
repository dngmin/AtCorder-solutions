R, X = map(int,input().split())

min, max = (1600, 2999) if X == 1 else (1200, 2399)

print("Yes" if min <= R <= max else "No")