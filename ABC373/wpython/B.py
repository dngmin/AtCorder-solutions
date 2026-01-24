S = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
current = S.index("A")
total = 0
for i in alphabet:
    next = S.index(i)
    total += abs(current - next)
    current = next
print(total)