N, Q = map(int,input().split())
move = 0
L, R = 1, 2

for _ in range(Q):
    H, T = input().split()
    T = int(T)
    if H == "R":
        H = R
        R = T
        offosite_hand = L
    else:
        H = L
        L = T
        offosite_hand = R

    if T > H:
        clockwise = T - H
    else:
        clockwise = N + T - H

    if T > H:
        counterclockwise = N - T + H
    else:
        counterclockwise = H - T

    if T > H:
        if H < offosite_hand < T:
            move += counterclockwise
        else:
            move += clockwise
    else:
        if T < offosite_hand < H:
            move += clockwise
        else:
            move += counterclockwise

print(move)