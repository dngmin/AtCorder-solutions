N, c1, c2 = map(str,input().split())
S = input()

output = ""
for i in S:
    output += c1 if i == c1 else c2
print(output)