def recursive_balanced_binary_tree(tree, key=0, depth=0):

    # depth first search
    if not tree[key]:
        return depth
    else:
        left = recursive_balanced_binary_tree(tree, tree[key][0], depth + 1)
        print "Left: %s" % left

        if len(tree[key]) == 2:
            right = recursive_balanced_binary_tree(tree, tree[key][1], depth + 1)
            print "Right: %s" % right
        else:
            right = depth

        if left > right + 1 or right > left + 1 or not right or not left:
            return False
        elif depth == 0:
            return True
        else:
            print "Returning depth: %s" % depth
            return max(left, right)


def balanced_binary_tree(tree):

    return True


def main():
    binary_tree = {
        0: [1, 2],
        1: [3, 4],
        2: [5, 6],
        3: [7, 8],
        4: [9, 10],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [11],
        11: []
    }

    print binary_tree
    print(balanced_binary_tree(binary_tree))  #


if __name__ == '__main__':
    main()
