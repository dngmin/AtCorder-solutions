N, S = map(int,input().split())
T_list = list(map(int,input().split()))
sleep = False

for i in range(len(T_list)):
    if i == 0:
        lapse = T_list[0]
    else:
        lapse = T_list[i] - T_list[i-1]
    if lapse > S:
        sleep = True
        break
print("Yes" if sleep == False else "No")