N = int(input())
S = input()
A_idx = []
for i in range(2*N):
    if S[i] == "A":
        A_idx.append(i)
swap1 = 0
swap2 = 0
for i in range(0,N):
    A_first = 2*i
    swap1 += abs(A_idx[i] - A_first)

    A_after = 2*i+1
    swap2 += abs(A_idx[i] - A_after)

print(min(swap1,swap2))