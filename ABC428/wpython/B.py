N, K = map(int,input().split())
S = input()

substring_count = {}

for i in range(0, N-K+1):
    if S[i:i+K] in substring_count:
        substring_count[S[i:i+K]] += 1
    else:
        substring_count[S[i:i+K]] = 1

x = max(substring_count.values())
x_list = list()
for j in substring_count.keys():
    if substring_count[j] == x:
        x_list.append(j)
x_list.sort()

print(x)
print(" ".join(x_list))