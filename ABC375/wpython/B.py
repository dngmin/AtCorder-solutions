N = int(input())
current_x = 0
current_y = 0
total_cost = 0

for _ in range(N):
    X, Y = map(int,input().split())
    total_cost += ((current_x - X)**2 + (current_y - Y)**2 )**(1/2)
    current_x = X
    current_y =Y
    
total_cost += ((current_x)**2 + (current_y)**2)**(1/2)

print(total_cost)