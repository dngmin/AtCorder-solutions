N, M = map(int,input().split())
A_list = list(map(int,input().split()))

if (sum(A_list)-M) in A_list:
    print('Yes')
else:
    print('No')