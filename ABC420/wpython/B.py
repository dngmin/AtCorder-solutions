N, M = map(int,input().split())

S_list = [input() for S in range(N)]
score_board = []
for i in range(N):
    score_board.append(0)

for i in range(M):
    voted = []
    for j in range(N):
        voted.append(S_list[j][i])
    count0 = voted.count('0')
    count1 = voted.count('1')
    if count0 == 0 or count1 == 0:
        pass
    elif count0 > count1:
        for j in range(N):
            if S_list[j][i] == '1':
                score_board[j] += 1
    else:
        for j in range(N):
            if S_list[j][i] == '0':
                score_board[j] += 1

winner = [i+1 for i in range(N) if score_board[i] == max(score_board)]
print(" ".join(map(str,winner)))