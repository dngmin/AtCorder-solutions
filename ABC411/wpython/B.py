N = int(input())
D = list(map(int,input().split()))
dis_list = []
for i in range(N-1):
    for j in range(i+1,N):
        dis_list.append(sum(D[i:j]))
    print(" ".join(map(str,dis_list)))
    dis_list = []