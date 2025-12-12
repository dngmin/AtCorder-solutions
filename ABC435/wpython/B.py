N = int(input())
A_list = list(map(int,input().split()))
No_Divisible = 0

for i in range(1,N):
    for j in range(0,N-i):
        divisible = False
        sum_l2r = sum(A_list[j:j+i+1])
        for A in A_list[j:j+i+1]:
            if sum_l2r%A == 0:
                divisible = True
                break
        if not divisible:
            No_Divisible += 1

print(No_Divisible)