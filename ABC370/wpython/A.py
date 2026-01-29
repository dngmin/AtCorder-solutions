L, R = map(int, input().split())
if L and not R:
    print("Yes")
elif not L and R:
    print("No")
else:
    print("Invalid")