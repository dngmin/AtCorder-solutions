W, B = map(int,input().split())
keyboard = "wbwbwwbwbwbw"

for i in range(len(keyboard)):
    w = 0
    b = 0
    for j in range(W+B):
        if keyboard[(i+j)%12] == "w":
            w += 1
        else:
            b += 1
    if w == W and b == B:
        print("Yes")
        break
else:
    print("No")