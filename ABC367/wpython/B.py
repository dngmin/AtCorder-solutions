X = input()
cutting = 0
for i in range(len(X)-1, len(X)-4, -1):
    if X[i] == "0":
        cutting += 1
    else:
        break

print(X if cutting == 0 else X[:-4] if cutting == 3 else X[:-cutting])