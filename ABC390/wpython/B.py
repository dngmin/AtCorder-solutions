N = int(input())
A_list = list(map(int,input().split()))
geometric_progression = True
for i in range(1,N-1):
    if A_list[i]*A_list[i] != A_list[i-1]*A_list[i+1]:
        geometric_progression = False
        break

print("Yes" if geometric_progression else "No")