X = int(input())
count = 0
for i in range(1,10):
    for j in range(1,10):
        count += 1 if X == i*j else 0
print(2025-X*count)