S = input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if not i in S:
        print(i)
        break