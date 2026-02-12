N, A = map(int, input().split())
T_list = list(map(int,input().split()))
waiting = False
time = 0
output = list()
for T in T_list:
    if time <= T:
        output.append(T+A)
        time = T+A
    else:
        output.append(time+A)
        time = time+A
for o in output:
    print(o)