import sys
sys.setrecursionlimit(10**7)

N = int(input())
skills = [False for _ in range(0,N+1)]

def set_skills(i):
    if skills[i] == False:
        skills[i] = True
    elif skills[i] == True:
        return
    else:
        for skill in skills[i]:
            skills[i] = True
            set_skills(skill)

for i in range(1,N+1):
    A, B = map(int,input().split())
    if A == B == 0 or skills[A] == True or skills[B] == True:
        set_skills(i)

    else:
        if skills[A] == False:
            skills[A] = {i}
        else:
            skills[A].add(i)
        if skills[B] == False:
            skills[B] = {i}
        else:
            skills[B].add(i)

print(skills.count(True))