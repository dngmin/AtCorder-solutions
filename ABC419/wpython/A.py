S = input()
known = {"red":"SSS","blue":"FFF","green":"MMM"}
if S in known.keys():
    print(known[S])
else:
    print("Unknown")