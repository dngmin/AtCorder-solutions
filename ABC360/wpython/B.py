S, T = map(str,input().split())
for w in range(len(S)-1):
    for c in range(w+1):
        s = ""
        i = c
        while i < len(S):
            s += S[i]
            i += w+1
        if s == T:
            print("Yes")
            exit()
print("No")