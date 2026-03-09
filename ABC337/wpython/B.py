S = input()
i = None
for s in S:
    if i == "B" and s == "A":
        print("No")
        break
    elif i == "C" and (s == "A" or s == "B"):
        print("No")
        break
    i = s
else:
    print("Yes")