N = int(input())
A_list = list(map(int,input().split()))
A_dict = dict.fromkeys(A_list)

answer = 0

for i in range(N):
    if A_dict[A_list[i]]:
        A_dict[A_list[i]] +=1
    else:
        A_dict[A_list[i]] = 1

for num_count in list(A_dict.values()):
    if num_count >=2:
        answer += int(num_count*(num_count-1)/2*(N-num_count))

print(answer)