N, K = map(int,input().split())
S = input()
i = 0
count = 0
while i < N-K+1:
    if S[i:i+K] == "O"*K:
        i += K
        count += 1
    else:
        i += 1
print(count)