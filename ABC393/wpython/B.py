S = input()
count = 0
if len(S)%2 == 0:
    max_step = int(len(S)/2)
else:
    max_step = int(len(S)/2+1)

for step in range(1,max_step):
    for i in range(0,len(S)-2*step):
        if S[i] == "A" and S[i+step] == "B" and S[i+2*step] == "C":
            count +=1

print(count)