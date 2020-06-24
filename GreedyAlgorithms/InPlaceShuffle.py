def inplaceshuffle(input):

    for index in input:
        randomindex = getrandom(0, len(input))

        if randomindex != index:
            temp = input[index]
            input[index] = input[randomindex]
            input[randomindex] = temp

    return input


# testing
arr1 = [3, 5, 7, 9, 10, 12, 14, 15, 17, 19, 21, 23, 25, 30]
arr2 = [1, 2, 3, 4, 5]

for x in range(5):
    print(inplaceshuffle(arr1), x)

for x in range(5):
    print(inplaceshuffle(arr2), x)
