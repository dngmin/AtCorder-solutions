X, Y, Z = map(int,input().split())

if (X-Y*Z)/(Z-1) >= 0 and (X-Y*Z)%(Z-1) == 0:
    print("Yes")
else:
    print("No")