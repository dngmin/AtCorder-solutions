N, M = map(int,input().split())
H_list = list(map(int,input().split()))
output = 0
for H in H_list:
    M -= H
    if M < 0:
        break
    output += 1
print(output)