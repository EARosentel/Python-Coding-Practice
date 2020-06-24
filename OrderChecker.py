def inorder (takeoutorders, dineinorders, servedorders):
    dineinindex = 0
    takeoutindex = 0

    for orderno in servedorders:
        if takeoutindex < len(takeoutorders) and orderno == takeoutorders[takeoutindex]:
            takeoutindex += 1
        elif dineinindex < len(dineinorders) and orderno == dineinorders[dineinindex]:
            dineinindex += 1
        else:
            return False

    return True


# testing
takeoutorders = [1, 7]
dineinorders = [2, 4, 6]
servedorders = [2, 4, 6, 7, 1]

print(inorder(takeoutorders,dineinorders,servedorders))