X, Y = map(int,input().split())

winner = set()

for i in range(1,7):
    for j in range(1,7):
        if i+j >= X or (i-j)**2 >= Y**2:
            winner.add(f"{i}{j}")

print(len(winner)/36)