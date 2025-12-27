S1, S2 = map(str,input().split())
print(1 if S1 == S2 == "sick" else 2 if S1 != S2 == "fine" else 3 if S1 != S2 == "sick" else 4 )