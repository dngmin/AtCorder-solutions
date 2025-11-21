Q = int(input())
query_list = [input() for i in range(Q)]
bag = []
for query in query_list:
    if query[0] == '1':
        _, x = map(int,query.split())
        bag.append(x)
    elif query[0] == '2':
        print(min(bag))
        bag.pop(bag.index(min(bag)))