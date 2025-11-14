N = int(input())

total = 0

for i in range(1,N+1):
    total += ((-1)**(i))*i**3

print(total)