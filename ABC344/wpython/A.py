S = input()
i = S.find("|")
j = S.find("|",i+1)
print(S[:i]+S[j+1:])