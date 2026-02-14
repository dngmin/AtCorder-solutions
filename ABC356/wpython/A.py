N, L, R = map(int,input().split())
A_list = [i+1 for i in range(N)]

output = A_list[:L-1]
output.extend(list(reversed(A_list[L-1:R])))
output.extend(A_list[R:])
print(" ".join(map(str,output)))