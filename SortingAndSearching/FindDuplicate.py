def find_duplicate(intarr):
    floor = -1
    ceiling = len(intarr)

    while floor < ceiling - 1:
        dist = (ceiling - floor) / 2
        guess = floor + dist

        if intarr[guess] == intarr[guess+1]:
            return intarr[guess]
        else:
            floor = guess


    return None


# testing
onedupe = [1,2,3,4,4,5,6]
manydupe = [1,1,1,3,3,3,6]

# print(find_duplicate(emptyarr))  # returns None
# print(find_duplicate(nodupes))  # returns None
print(find_duplicate(onedupe))  # returns 4
print(find_duplicate(manydupe))  # returns 1
