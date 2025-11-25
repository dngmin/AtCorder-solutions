S = input()
S_list = []
len_S = len(S)
count_nsign = [0]*(len_S+1)
for i in range(len_S):
    count_nsign[i+1] = count_nsign[i] + (1 if S[i] == "#" else 0)

for i in range(len_S):
    if S[i] == "#":
        S_list.append("#")
    elif i+1 != len_S and S[i+1] == "#":
        S_list.append("o")
    elif count_nsign[-1] - count_nsign[i] == 0:
        if (1 != 0 and S[i-1] == "#") or i == 0:
            S_list.append("o")
        else:
            S_list.append(".")
    else:
        S_list.append(".")

print("".join(map(str,S_list)))