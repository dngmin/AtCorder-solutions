N = int(input())
S = input()
i = int((N+1)/2 -1)
if N%2 != 0 and S[i] == "/" and S[:i] == "1"*i and S[i+1:] == "2"*i:
    print("Yes")
else:
    print("No")