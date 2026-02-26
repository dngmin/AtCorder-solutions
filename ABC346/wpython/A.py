N = int(input())
A_list = list(map(int,input().split()))
B_list = list()
for i in range(N-1):
    B_list.append(str(A_list[i]*A_list[i+1]))
print(" ".join(B_list))