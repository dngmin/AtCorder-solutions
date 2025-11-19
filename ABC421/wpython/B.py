X, Y = map(int,input().split())

def rev(x):
    x = str(x)
    x_ = []

    for i in range(len(x)-1,-1,-1):
        x_.append(x[i])

    while x_[0] == 0:
        x_.pop(0)

    return int("".join(x_))

for i in range(8):
    a_i = rev(X+Y)
    X = Y
    Y = a_i

print(a_i)