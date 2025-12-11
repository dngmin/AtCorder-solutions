N, M = map(int,input().split())

binarys = [format(i,f'0{N+1}b') for i in range(2**N)]
minimum = M
u_list = []
v_list = []
for i in range(M):
    u, v = map(int,input().split())
    u_list.append(u)
    v_list.append(v)

for binary in binarys:
    current = 0
    for i in range(M):
        if binary[u_list[i]] == binary[v_list[i]]:
            current += 1
    if current < minimum:
        minimum = current

print(minimum)