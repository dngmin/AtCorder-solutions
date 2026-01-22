N = int(input())
S = input()
output = 0
for i in range(0,N-2):
    if S[i] == S[i+2] == "#" and S[i+1] == ".":
        output += 1
print(output)