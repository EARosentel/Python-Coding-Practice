def binary_search(target, list):
    floor_index = -1
    ceiling_index = len(list)

    while floor_index < ceiling_index:
        halfdist = (ceiling_index - floor_index)/2
        if halfdist == 0:
            return False
        guess_index = floor_index + halfdist

        guess_val = list[guess_index]

        if guess_val == target:
            return True

        if guess_val > target:
            ceiling_index = guess_index
        else:
            floor_index = guess_index

    return False


# testing
numlist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

print(binary_search(3, numlist))  # true
print(binary_search(8, numlist))  # false
print(binary_search(1, numlist))  # true
print(binary_search(2, numlist))  # false
print(binary_search(-1, numlist))  # false
print(binary_search(200, numlist))  # false


