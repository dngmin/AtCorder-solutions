N = int(input())
feel_sick = False
ex_food = None
for i in range(N):
    cur_food = input()
    if ex_food == cur_food == "sweet" and i != N-1:
        feel_sick = True
    ex_food = cur_food
print("Yes" if not feel_sick else "No")