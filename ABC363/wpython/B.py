N, T, P = map(int,input().split())
L_list = list(map(int,input().split()))
distribution = [0]*(max(L_list)+1)
for L in L_list:
    distribution[L] += 1
day = 0
while sum(distribution[T-day:]) < P:
    day += 1
print(day)