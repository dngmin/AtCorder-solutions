N = int(input())
S_list= []
T = 0
for _ in range(N):
    S, C = input().split()
    S_list.append(S)
    T += int(C)
S_list.sort()
print(S_list[T%N])