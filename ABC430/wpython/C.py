N, A, B = map(int,input().split())
S = input()
count=0

count_a = [0] * (N+1)
count_b = [0] * (N+1)

for i in range(N):
    count_a[i+1] = count_a[i] + (1 if S[i] == "a" else 0)
    count_b[i+1] = count_b[i] + (1 if S[i] == "b" else 0)

def A_count(l,r):
    return count_a[r] - count_a[l]
def B_count(l,r):
    return count_b[r] - count_b[l]

ra = 0
rb = 0
for l in range(N-A+1):
    rb = max(ra,rb)
    while ra < N and A_count(l,ra) < A:
        ra += 1
    if ra == N and A_count(l,ra) < A:
            break
    while rb < N and B_count(l,rb) < B:
        rb += 1
    if rb == N:
        if A_count(l,ra) == A and B_count(l,rb) == B:
            count += rb - ra
        elif rb > ra:
            count += rb - ra + 1
        elif ra == N:
            count += 1
    elif rb > ra:
        count += rb - ra
print(count)