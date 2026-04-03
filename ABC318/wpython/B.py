N = int(input())
sheets = [list(map(int,input().split())) for _ in range(N)]
overlapped_area = set()

for sheet in sheets:
    A, B, C, D = sheet
    for i in range(A,B):
        for j in range(C,D):
            overlapped_area.add(f"{i}.{j}")
print(len(overlapped_area))