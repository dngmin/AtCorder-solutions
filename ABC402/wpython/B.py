Q = int(input())
waiting = []
answer = []
for i in range(Q):
    query = input()
    if query[0] == '1':
        _, menu = map(int,query.split())
        waiting.append(menu)
    else:
        answer.append(waiting[0])
        waiting.pop(0)
print("\n".join(map(str,answer)))