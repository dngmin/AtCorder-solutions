N = int(input())
C_list = [list(map(int,input().split())) for _ in range(N-1)]

for a in range(0,N-2):
    for b in range(a+1,N-1):
        for c in range(b+1,N):
            if C_list[a][c-a-1] > C_list[a][b-a-1] + C_list[b][c-b-1]:
                print("Yes")
                exit()
print("No")