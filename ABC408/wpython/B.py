N = int(input())
A_list = list(map(int,input().split()))
A_list.sort()
A_sort = list(dict.fromkeys(A_list))

print(len(A_sort))
print(" ".join(map(str,A_sort)))