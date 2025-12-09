N = int(input())
A_list = list(map(int,input().split()))
sum = A_list[0]

for i in range(1,round(N/2)):
    sum += A_list[2*i]
print(sum)