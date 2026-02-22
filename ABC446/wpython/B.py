N, M = map(int,input().split())
juice = [True] * (M+1)
output = list()
for _ in range(N):
    get = 0
    L = int(input())
    X = list(map(int,input().split()))
    for x in X:
        if juice[x]:
            juice[x] = False
            get = x
            break
    output.append(get)
for i in output:
    print(i)