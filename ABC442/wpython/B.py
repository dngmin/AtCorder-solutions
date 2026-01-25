Q = int(input())
outputs = []
vol = 0
playing = False

for _ in range(Q):
    A = int(input())
    if A == 1:
        vol += 1
    elif A == 2:
        vol += 0 if vol == 0 else -1
    else:
        if playing:
            playing = False
        else:
            playing = True
    outputs.append("Yes" if vol >= 3 and playing else "No")

for output in outputs:
    print(output)