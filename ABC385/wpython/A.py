ABC_list = list(map(int,input().split()))
print("Yes" if sum(ABC_list) - max(ABC_list)*2 == 0
      or len(set(ABC_list)) == 1
      else "No")