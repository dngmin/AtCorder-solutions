N = int(input())
A_list = list(map(int,input().split()))
A_max_idx = A_list.index(max(A_list))
A_list[A_max_idx] = 0
print(A_list.index(max(A_list))+1)