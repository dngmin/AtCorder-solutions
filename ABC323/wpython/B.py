N = int(input())
S_list = [input() for _ in range(N)]
win_count = [[] for _ in range(N)]
for i,S in enumerate(S_list):
    win_count[(N-1) - S.count('o')].append(i+1)

for win in win_count:
    for player in win:
        print(player, end=" ")