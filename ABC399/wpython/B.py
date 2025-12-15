N = int(input())
P_list = list(map(int,input().split()))
score_list = list(set(P_list))
score_list.sort(reverse=True)
ranks = [0]*N
r = 1
count = 0

for score in score_list:
    for i in range(N):
        if P_list[i] == score:
            ranks[i] = r
            count += 1
    r += count
    count = 0

for rank in ranks:
    print(rank)