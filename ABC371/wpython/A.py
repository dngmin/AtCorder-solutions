Sab, Sac, Sbc = map(str,input().split())

A, B, C = 0, 0, 0

if Sab == "<":
    B += 1
else:
    A += 1
if Sac == "<":
    C += 1
else:
    A += 1
if Sbc == "<":
    C += 1
else:
    B += 1

if A == 1:
    print("A")
elif B == 1:
    print("B")
else:
    print("C")