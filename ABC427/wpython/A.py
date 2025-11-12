S = input()

print(
    S.replace(
        S[0:int((len(S)-1)/2)+1],
        S[0:int((len(S)-1)/2)]
        )
    )