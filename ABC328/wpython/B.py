N = int(input())
D_list = list(map(int,input().split()))
D_list.insert(0,0)
output = 0
for M in range(1,N+1):
    if M < 10:
        if D_list[M] < M:
            output += 0
        elif D_list[M] < M*11:
            output += 1
        else:
            output += 2
    elif M%11 == 0:
        if D_list[M] < M//11:
            output += 0
        elif D_list[M] < M:
            output += 1
        else:
            output += 2
print(output)