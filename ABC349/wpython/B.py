S = input()
element = dict()
for s in S:
    element[s] = 0
for s in S:
    element[s] += 1
for e in set(element.values()):
    if list(element.values()).count(e) != 2:
        print("No")
        break
else:
    print("Yes")