N = int(input())
A = list(map(int,input().split()))

P =  [None if Pn == -1 else Pn for Pn in A]
for i in range(1,N+1):
    if i in P:
        continue
    else:
        try:
            P[P.index(None)] = i
        except:
            print("No")
            exit()

print("Yes")
print(" ".join(map(str,P)))