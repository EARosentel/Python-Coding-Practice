def highestproduct(inputarray):
    lowestnumber = min(inputarray[0], inputarray[1])
    highestnumber = max(inputarray[0], inputarray[1])
    highestoftwo = inputarray[0]*inputarray[1]
    lowestoftwo = highestoftwo
    highestofthree = highestoftwo*inputarray[2]

    print("input: ", inputarray)
    print("highest number: ", highestnumber)
    print("lowest number: ", lowestnumber)
    print("highest of two: ", highestoftwo)
    print("lowest of two: ", lowestoftwo)
    print("highest of three: ", highestofthree)

    for x in range(2, len(inputarray)):
        thisnum = inputarray[x]
        if thisnum * highestoftwo > highestofthree and x > 2:
            highestofthree = thisnum*highestoftwo
            print("x: - new highest of three: ", x, highestofthree)
        if thisnum * lowestoftwo > highestofthree and x > 2:
            highestofthree = thisnum * highestoftwo
            print("x: - new highest of three: ", x, highestofthree)

        if thisnum*highestnumber > highestoftwo:
            highestoftwo = thisnum*highestnumber
            print("x: - new highest of two: ", x, highestoftwo)
        if thisnum * lowestnumber > highestoftwo:
            highestoftwo = thisnum * lowestnumber
            print("x: - new highest of two: ", x, highestoftwo)

        if thisnum*lowestnumber < lowestoftwo:
            lowestoftwo = thisnum * lowestnumber
            print("x: - new lowest of two: ", x, lowestoftwo)
        elif thisnum * highestnumber < lowestoftwo:
            lowestoftwo = thisnum * highestnumber
            print("x: - new lowest of two: ", x, lowestoftwo)

        if thisnum > highestnumber:
            highestnumber = thisnum
            print("x: - new highest number: ", x, highestnumber)
        if thisnum < lowestnumber:
            lowestnumber = thisnum
            print("x: - new lowest number: ", x, lowestnumber)



    return highestofthree


# testing
input1 = [2, 4, 6, 10]
input2 = [-1, 20, -10, 2, 4]
input3 = [-2, -4, -6, -10, 1]

print(highestproduct(input1))  # should return 4 * 6 * 10 = 240
print(highestproduct(input2))  # should return -1 * 20 * -10 = 200
print(highestproduct(input3))  # should return -6 * -10 * 1 = 60
