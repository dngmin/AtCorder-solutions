N, H, X = map(int,input().split())
P_list = list(map(int,input().split()))

for i in range(len(P_list)):
    if P_list[i] >= X-H:
        print(i+1)
        break