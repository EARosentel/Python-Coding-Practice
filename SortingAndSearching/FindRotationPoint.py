def findRotationPoint(wordarr):
    floor = -1
    ceiling = len(wordarr)

    if len(wordarr) == 0:
        return -1

    firstword = wordarr[0]

    while floor <= ceiling:
        dist = (ceiling-floor)/2

        if dist == 0:
            break

        guess = floor + dist

        if wordarr[guess] < firstword:
            ceiling = guess

        else:
            floor = guess

    if ceiling >= len(wordarr):
        return 0

    return ceiling


# testing
wordarr1 = []
wordarr2 = ["find", "ghost", "igloo", "jealous", "alphabet", "better", "careen", "delve", "echo"]
wordarr3 = ["dance", "dancing", "dancer", "dances", "egg", "eggs", "eggy", "caravan"]
wordarr4 = ["alpha", "beta", "delta"]

print(findRotationPoint(wordarr1))  # -1
print(findRotationPoint(wordarr2))  # 4
print(findRotationPoint(wordarr3))  # 7
print(findRotationPoint(wordarr4))  # 0
