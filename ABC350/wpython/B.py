N, Q = map(int,input().split())
Teeth = [True]*(N+1)
Teeth[0] = N
T_list = list(map(int,input().split()))

for T in T_list:
    if Teeth[T]:
        Teeth[T] = False
        Teeth[0] -= 1
    else:
        Teeth[T] = True
        Teeth[0] += 1
print(Teeth[0])