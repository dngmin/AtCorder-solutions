N = int(input())
S_list = [input() for _ in range(N)]
S_set = set()

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if "".join([S_list[i],S_list[j]]) in S_set:
            continue
        else:
            S_set.add("".join([S_list[i],S_list[j]]))
print(len(S_set))