Q = int(input())
S = []
answer = []
good_bracket = 0
False_point = False
for i in range(Q):
    query = list(map(str,input().split()))
    if query[0] == '1':
        S.append(query[1])
        if query[1] == "(":
            good_bracket +=1
        else:
            good_bracket -=1
    else:
        if S[-1] == "(":
            good_bracket -=1
        else:
            good_bracket +=1
        S.pop()
    
    if False_point == False and good_bracket < 0:
        False_point = len(S)
    elif False_point:
        if len(S) < False_point:
            False_point = False 

    if False_point or good_bracket != 0:
        answer.append("No")
    else:
        answer.append("Yes")

for a in answer:
    print(a)