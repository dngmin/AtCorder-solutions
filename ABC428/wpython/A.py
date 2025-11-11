S, A, B, X = map(int,input().split())
distance = 0
while X > 0:
    if (X-A) >= 0:
        distance += S*A
        X -= A
    else:
        distance += S*X
        break
    if (X-B) >= 0 :
        X -= B
    else:
        break
print(distance)