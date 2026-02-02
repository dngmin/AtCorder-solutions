A, B, C = map(int, input().split())
output = None
if B < C:
    if B < A < C:
        output = "No"
    else:
        output = "Yes"
else:
    if C < A < B:
        output = "Yes"
    else:
        output = "No"
print(output)