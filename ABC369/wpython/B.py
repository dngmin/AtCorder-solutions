N = int(input())
past_L = None
past_R = None
fatigue = 0

for _ in range(N):
    A, S = map(str, input().split())
    A = int(A)
    if S == "R":
        fatigue += abs(past_R - A) if past_R else 0
        past_R = A
    else:
        fatigue += abs(past_L - A) if past_L else 0
        past_L = A
print(fatigue)