N = int(input())
smallest_RC = [10**9,10**9]
biggest_RC = [0,0]
for _ in range(N):
    R, C = map(int,input().split())
    if R < smallest_RC[0]:
        smallest_RC[0] = R
    if C < smallest_RC[1]:
        smallest_RC[1] = C
    if R > biggest_RC[0]:
        biggest_RC[0] = R
    if C > biggest_RC[1]:
        biggest_RC[1] = C
print(max(biggest_RC[0] - (biggest_RC[0]+smallest_RC[0])//2,biggest_RC[1] - (biggest_RC[1]+smallest_RC[1])//2))