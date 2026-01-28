N, M = map(int,input().split())
taro = [True for _ in range(N+1)]
outputs = []
for _ in range(M):
    check = "No"
    A, B = map(str,input().split())
    if B == "M":
        if taro[int(A)]:
            taro[int(A)] = False
            check = "Yes"
    outputs.append(check)
for output in outputs:
    print(output)