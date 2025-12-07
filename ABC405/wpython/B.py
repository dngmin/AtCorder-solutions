N, M = map(int,input().split())

A_list = list(map(int,input().split()))

count = [0] * (M+1)
operation = 0

for A in A_list:
    count[A] += 1

while True:
    if 0 in count[1:]:
        break
    count[A_list[-1]] -= 1
    operation += 1
    A_list.pop()

print(operation)