N = int(input())
A_list = list(map(int,input().split()))
output = 0
for i in range(len(A_list)-2):
    output += 1 if A_list[i] == A_list[i+2] else 0
print(output)