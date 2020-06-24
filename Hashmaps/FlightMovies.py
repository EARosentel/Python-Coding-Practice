def inflightmovies(flightlength, movielengths):
    lengthset = set()
    for movie in movielengths:
        if movie in lengthset:
            return True
        else:
            lengthset.add(flightlength - movie)
    return False


# testing
flightlength = 100
movielengths = [60, 41, 100, 75, 45, 105]
print(inflightmovies(flightlength, movielengths))
