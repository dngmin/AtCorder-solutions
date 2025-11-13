X, Y = map(str,input().split())

released_version = ["Ocelot", "Serval", "Lynx"]

if released_version.index(X)<released_version.index(Y):
    print("No")
else:
    print("Yes")