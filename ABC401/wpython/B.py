N = int(input())
login = False
error = 0

for _ in range(N):
    S = input()
    if S == "login":
        login = True
    elif S == "logout":
        login = False
    elif S == "private" and login == False:
        error += 1
print(error)