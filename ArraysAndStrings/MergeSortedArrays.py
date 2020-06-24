
print("save four")

def mergearrays(arr1, arr2):
    result = []
    totallength = len(arr1) + len(arr2)
    index1 = 0
    index2 = 0
    currentlength = 0

    print("total length: ", totallength)

    while currentlength < totallength:
        if index1 <= len(arr1) and (index2 >= len(arr2) or arr1[index1] < arr2[index2]):
            result.append(arr1[index1])
            index1 += 1
        else:
            result.append(arr2[index2])
            index2 += 1

        currentlength += 1
        print("index 1: ", index1, " index 2: ", index2, " current length: ", currentlength)
        print(result)

    return result


# testing
arr1 = [-1, 3, 7, 9, 13, 16]
arr2 = [-2, 6, 8, 12]

result = mergearrays(arr1, arr2)

print(result)


