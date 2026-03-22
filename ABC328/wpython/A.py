N, X = map(int,input().split())
S_list = list(map(int,input().split()))
output = 0
for S in S_list:
    output += S if S <= X else 0
print(output)