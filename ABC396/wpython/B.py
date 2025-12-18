Q = int(input())
deck = [0]*Q
output = list()
for _ in range(Q):
    q = input()
    if q[0] == '2':
        output.append(deck[-1])
        deck.pop()
    else:
        deck.append(list(map(int,q.split()))[-1])
for i in output:
    print(i)