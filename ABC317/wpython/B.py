N = int(input())
A_list = list(map(int,input().split()))
A_list.sort()
if A_list == list(range(A_list[0],A_list[-1]+1)):
    print(A_list[0]-1 if A_list[0] != 1 else A_list[-1]+1)
else:
    i = A_list[0]
    for A in A_list:
        if i == A:
            i += 1
        else:
            print(i)
            break