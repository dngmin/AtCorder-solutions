D = input()
direction = ["N","NE","E","SE","S","SW","W","NW"]
print(direction[(direction.index(D)+4)%8])