N, K = map(int,input().split())
A_list = list(map(int,input().split()))
empty_seat = K
output = 1
for A in A_list:
    if empty_seat >= A:
        empty_seat -= A
    else:
        output += 1
        empty_seat = K - A
print(output)