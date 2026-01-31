N = int(input())
A = list(map(int, input().split()))
count = 0
while sum(A) != max(A):
    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1
    count += 1
print(count)