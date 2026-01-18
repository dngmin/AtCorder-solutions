N, M = map(int,input().split())
S_set = set([s for s in input()])
T_set = set([t for t in input()])
output = []
for _ in range(int(input())):
    w = set([W for W in input()])
    if w&S_set == w&T_set:
        output.append("Unknown")
    elif w&S_set == w:
        output.append("Takahashi")
    elif w&T_set == w:
        output.append("Aoki")
        
for o in output:
    print(o)