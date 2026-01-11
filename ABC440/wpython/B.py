N = int(input())
T_list = list(map(int,input().split()))
T_rank = {
    "horse" : [],
    "time" : [200,200,200]
}
for horse, time in enumerate(T_list,start=1):
    if time <= T_rank["time"][2]:
        if time <= T_rank["time"][1]:
            if time <= T_rank["time"][0]:
                T_rank["horse"].insert(0,horse)
                T_rank["time"].insert(0,time)
            else:
                T_rank["horse"].insert(1,horse)
                T_rank["time"].insert(1,time)
        else:
            T_rank["horse"].insert(2,horse)
            T_rank["time"].insert(2,time)
print(" ".join(map(str,T_rank["horse"][0:3])))