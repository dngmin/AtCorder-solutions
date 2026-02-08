xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())

lAB = (xA-xB)**2 + (yA-yB)**2
lAC = (xA-xC)**2 + (yA-yC)**2
lBC = (xB-xC)**2 + (yB-yC)**2

print("Yes" if sum([lAB,lAC,lBC]) == max(lAB,lAC,lBC)*2 else "No")