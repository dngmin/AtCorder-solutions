X = input()
X_element = []

for i in range(0,len(X)):
    X_element.append(int(X[i]))

X_element.sort()

if X_element[0] == 0:
    first = X_element[X_element.count(0)]
    X_element.remove(first)
    X_element.insert(0,first)

print(int("".join(list(map(str,X_element)))))