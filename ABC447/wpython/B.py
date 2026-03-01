S = input()
S_dict = {}
output = ""
for s in S:
    if s in S_dict:
        S_dict[s] += 1
    else:
        S_dict[s] = 1
most_frequent = max(S_dict.values())
for s in S:
    if S_dict[s] != most_frequent:
        output += s
print(output)