N, Q = map(int,input().split())
X_list = list(map(int,input().split()))
box = [0]*(N)
history = []

for ball in X_list:
    if ball == 0:
        min_index = box.index(min(box))
        box[min_index] += 1
        history.append(min_index+1)
    else:
        box[ball-1] += 1
        history.append(ball)
print(" ".join(map(str,history)))