N = int(input())
T = input()
A = input()
both = False
for i in range(N):
    if T[i] == 'o' and A[i] == 'o':
        both = True
        break
if both:
    print("Yes")
else:
    print("No")