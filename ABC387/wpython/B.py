S = input()
i = 0
push_count = 0
while i < len(S):
    if i == len(S)-1:
        push_count += 1
        break
    i += 2 if S[i] == S[i+1] == "0" else 1
    push_count += 1
print(push_count)