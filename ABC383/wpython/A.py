N = int(input())

last_time, water = map(int,input().split())

for i in range(N-1):
    T, V = map(int,input().split())
    water = water -1*(T-last_time) + V if water -1*(T-last_time) >= 0 else V
    last_time = T

print(water)