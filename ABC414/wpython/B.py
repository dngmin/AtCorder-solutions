N = int(input())
S_length = 0
element = []
for _ in range(N):
    c, l = input().split()
    l = int(l)
    S_length += l

    if S_length <= 100:
        element.append(c*l)
        
if S_length > 100:
    print("Too Long")
else:
    print("".join(element))