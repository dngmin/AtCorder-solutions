S = input()
S_element = set()
string1122 = True
if len(S)%2 == 0:
    for i in range(1,len(S)//2+1):
        if S[2*i-2] == S[2*i-1]:
            S_element.add(S[2*i-2])
            continue
        else:
            string1122 = False
            break
    if len(S_element) != len(S)//2:
        string1122 = False
else:
    string1122 = False
print("Yes" if string1122 else "No")