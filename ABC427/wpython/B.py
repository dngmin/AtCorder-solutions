N = input()

def sum_of_digits(total,N):
    total = int(total)
    for i in range(0,len(N)):
        total += int(N[i])
    return str(total)

total = '1'

for i in range(0,int(N)-1):
    total = sum_of_digits(total,total)

print(total)