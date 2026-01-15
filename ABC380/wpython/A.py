N = input()
element = [n for n in N]
print("Yes" if element.count("1") == 1 and element.count("2") == 2 and element.count("3") == 3 else "No")
