S = input()
warehouse_info = [0]*(len(S)+1)
for i in range(len(S)):
    warehouse_info[i+1] = warehouse_info[i] + (1 if S[i] == "#" else 0)

pack1 = 0
pack2 = 0

while warehouse_info[-1] - warehouse_info[pack2+1] != 0:
    while S[pack1] == ".":
        pack1 +=1
    pack2 = pack1+1
    while S[pack2] == ".":
        pack2 +=1
    print(f"{pack1+1},{pack2+1}")
    pack1 = pack2 + 1