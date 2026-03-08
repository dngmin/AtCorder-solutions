N, M = map(int,input().split())
C_list = list(map(int,input().split()))
C_list.insert(0,0)
total = 0
for _ in range(N):
    A, B = map(int,input().split())
    if C_list[A] > B:
        total += B
        C_list[A] -= B
    else:
        total += C_list[A]
        C_list[A] = 0
print(total)