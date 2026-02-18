N = int(input())
H_list = list(map(int,input().split()))
for i in range(N):
    if H_list[0] < H_list[i]:
        print(i+1)
        break
else:
    print(-1)