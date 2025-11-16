A, B, C = map(int,input().split())

value = [A,B,C]
value.sort()
value.reverse()
max = value[0]*100 + value[1]*10 + value[2]
print(max)