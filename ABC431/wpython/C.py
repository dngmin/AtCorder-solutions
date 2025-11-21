N, M, K = map(int,input().split())
H_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
H_list.sort()
B_list.sort()
count = 0
plus_idx = 0
try:
    for i in range(N if N<M else M):
        if B_list[-1] < H_list[i]:
            raise ValueError
        elif H_list[i] > B_list[i+plus_idx]:
            while H_list[i] > B_list[i+plus_idx]:
                plus_idx += 1
        count +=1
        if count == K:
            print("Yes")
            break
except:
    print("No")
    exit()