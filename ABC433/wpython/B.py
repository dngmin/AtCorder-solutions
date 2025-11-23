N = int(input())
A_list = list(map(int,input().split()))

for i in range(N):
    existence = None
    if i == 0:
        print(-1)
    else:
        for j in range(i-1,-1,-1):
            if A_list[i] < A_list[j]:
                existence = j+1
                break
        if existence:
            print(existence)
        else:
            print(-1)