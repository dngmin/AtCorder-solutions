N, K = map(int, input().split())
cards = list(map(int, input().split()))
print(" ".join(map(str, cards[-K:])), " ".join(map(str, cards[:N-K])))