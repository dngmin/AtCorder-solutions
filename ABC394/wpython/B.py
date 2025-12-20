N = int(input())

S_list = dict()

for i in range(N):
    S = input()
    lens = len(S)
    S_list[lens] = S

len_idx = sorted(S_list)
print("".join([S_list[idx] for idx in len_idx]))