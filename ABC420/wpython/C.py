N, Q = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
zipped = list(zip(A_list,B_list))
zipped.insert(0,(0,0))
sum_of_min = 0
output = []

for A,B in zipped:
    sum_of_min += min(A,B)

for _ in range(Q):
    c, X, V = input().split()
    X, V = map(int, (X,V))

    sum_of_min -= min(zipped[X])
    if c == "A":
        zipped[X] = (V, zipped[X][1])
    else:
        zipped[X] = (zipped[X][0], V)
    sum_of_min += min(zipped[X])
    output.append(sum_of_min)

for o in output:
    print(o)