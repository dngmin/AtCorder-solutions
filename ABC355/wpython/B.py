N, M = map(int,input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
C_list = A_list.copy()
C_list.extend(B_list)
C_list.sort()

for A in A_list:
    C_list[C_list.index(A)] = 'A'

for i in range(len(C_list)-1):
    if C_list[i] == C_list[i+1]:
        print("Yes")
        break
else:
    print("No")