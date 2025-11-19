N = int(input())
name_list = [input() for _ in range(N)]

X , Y = input().split()

if name_list[int(X)-1] == Y:
    print("Yes")
else:
    print("No")