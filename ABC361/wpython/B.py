a, b, c, d, e, f = map(int,input().split())
g, h, i, j, k, l = map(int,input().split())

C1_range = {
    "x" : {i for i in range(min(a,d),max(a,d)+1)},
    "y" : {i for i in range(min(b,e),max(b,e)+1)},
    "z" : {i for i in range(min(c,f),max(c,f)+1)}
}
C2_range = {
    "x" : {i for i in range(min(g,j),max(g,j)+1)},
    "y" : {i for i in range(min(h,k),max(h,k)+1)},
    "z" : {i for i in range(min(i,l),max(i,l)+1)}
}

if len(C1_range["x"] & C2_range["x"]) > 1 and len(C1_range["y"] & C2_range["y"]) > 1 and len(C1_range["z"] & C2_range["z"]) > 1:
    print("Yes")
else:
    print("No")