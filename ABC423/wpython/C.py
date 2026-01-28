N, R = map(int,input().split())
L_list = list(map(int,input().split()))
count = 0

if R != 0:
    front_str = "".join(map(str,L_list[:R]))
    front = int(front_str, 2)
    if "0" in front_str:
        for _ in range(len(front_str) - front_str.find("0")):
            count += 2 if front & 1 == 1 else 1
            front >>= 1

if R != N:
    back_str = "".join(map(str,L_list[R:]))[::-1]
    back = int(back_str, 2)
    if "0" in back_str:
        for _ in range(len(back_str) - back_str.find("0")):
            count += 2 if back & 1 == 1 else 1
            back >>= 1

print(count)