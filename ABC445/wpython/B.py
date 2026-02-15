N = int(input())
m = 0
S_list = list()
for _ in range(N):
    S = input()
    m = len(S) if len(S) > m else m
    S_list.append(S)
for S in S_list:
    print("."*((m-len(S))//2)+S+"."*((m-len(S))//2))