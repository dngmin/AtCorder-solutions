S = input()

S_element = set([i for i in S])

if S[0] == S[1]:
    S_element.remove(S[0])
elif S[0] == S[2]:
    S_element.remove(S[0])
else:
    S_element.remove(S[1])

print("".join(map(str,S_element)))