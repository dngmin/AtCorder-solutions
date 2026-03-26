N = int(input())
A_list = list(map(int,input().split()))
jmAj_list = list()
ipAi_list = list()
for i in range(N):
    jmAj_list.append(i-A_list[i])
    ipAi_list.append(i+A_list[i])
jmAj_set = set(jmAj_list)
init_dict = dict()
find_list = list()
for jmAj in jmAj_set:
    init_dict[jmAj] = 0

for i in range(N):
    if ipAi_list[i] in init_dict:
        init_dict[ipAi_list[i]] += 1
    find_list.append(init_dict)

output = 0

for j in range(N):
    output += find_list[j][jmAj_list[j]]
print(output)