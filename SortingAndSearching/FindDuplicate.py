def find_duplicate(int_arr):
    floor = -1
    ceiling = len(int_arr)

    while floor < ceiling - 1:
        print "floor: %s  ceiling: %s" % (floor, ceiling)
        dist = (ceiling - floor) / 2
        guess = floor + dist
        if int_arr[guess] < guess + 1:
            ceiling = guess
        else:
            floor = guess

    return ceiling


def main():
    one_duplicate = [1, 1, 2, 2, 4, 5, 6]
    print(find_duplicate(one_duplicate))  # returns 4


if __name__ == '__main__':
    main()

