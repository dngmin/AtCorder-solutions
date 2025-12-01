N, M = map(int,input().split())
bird_count = [0] * M
sum_weight = [0] * M
for i in range(N):
    A, B = map(int,input().split())
    bird_count[A-1] += 1
    sum_weight[A-1] += B

for i in range(M):
    print(sum_weight[i]/bird_count[i])