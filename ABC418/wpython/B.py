S = input()
S_list= list(S[i] for i in range(len(S)))
t_idx_list = []

answer = 0

if S_list.count('t') >= 3:
    t_idx = 0
    while len(t_idx_list) < S_list.count('t'):
        t_idx = S_list.index('t',t_idx)
        t_idx_list.append(t_idx)
        t_idx += 1
    
    for i in t_idx_list[:-2]:
        for j in t_idx_list[2:]:
            if i+1>=j:
                continue
            filling_rate = (S[i:j+1].count('t') - 2) / (len(S[i:j+1]) - 2)
            if filling_rate > answer:
                answer = filling_rate

print(answer)