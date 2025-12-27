N, Q = map(int,input().split())
prefix = [1 for _ in range(0,N+1)]
outputs = [0]*Q
zeros_till = 0

for i in range(Q):
    X, Y = map(int,input().split())
    if X <= zeros_till:
        outputs[i] = 0
    else:
        val = sum(prefix[zeros_till+1:X+1])
        outputs[i] = val
        prefix[Y] += val
        zeros_till = X

for output in outputs:
    print(output)