def productsexceptatindex(input):
    print("input: ", input)
    resultarr = [1] * len(input)

    productsofar = 1
    for x in range(0, len(input)):
        resultarr[x] = productsofar
        productsofar *= input[x]

    productsofar = 1
    for y in range((len(input)-1), -1, -1):
        resultarr[y] *= productsofar
        productsofar *= input[y]

    return resultarr


# testing
input1 = [2, 3, 5, 7]  # length 4 - result 105
input2 = [1, -1, -5, 10]  # length 4 - result 50
input3 = [0, -5, 10, -15, 2]  # length 5 - result 1500

print(productsexceptatindex(input1))
print(productsexceptatindex(input2))
print(productsexceptatindex(input3))
