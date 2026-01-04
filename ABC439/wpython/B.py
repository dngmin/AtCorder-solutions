N = input()
happy_process = []
current = N
while not (current in happy_process):
    happy_process.append(current)
    output = 0
    for i in range(len(current)):
        output += int(current[i])*int(current[i])
    current = str(output)
print("Yes" if output == 1 else "No")