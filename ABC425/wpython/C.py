N, Q = map(int,input().split())
A_list = list(map(int,input().split()))
A_sum = [0]
for i in range(N):
    A_sum.append(A_sum[-1]+A_list[i])
answer = list()
starting = 0
for _ in range(Q):
    query = input()
    if query[0] == '1':
        _, c = map(int,query.split())
        starting = (starting + c)%N
    else:
        _, l, r = map(int,query.split())
        if starting+r <= N:
           value = A_sum[starting+r] - A_sum[starting+l-1]
        else:
            l = (starting + l)%N if (starting + l)%N !=0 else N
            r = (starting + r)%N if (starting + r)%N !=0 else N

            if l <= r:
                value = A_sum[r] - A_sum[l-1]
            else:
                value = A_sum[-1] - A_sum[l-1] + A_sum[r]
        answer.append(value)
for output in answer:
    print(output)