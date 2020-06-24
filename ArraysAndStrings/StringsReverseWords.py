# Objective: reverse the string in place
# Assumptions: there are only characters and spaces in the char array

print("save 3")

def reversechars(leftindex, rightindex, message):
    while leftindex < rightindex:
        tempchar = message[rightindex]
        message[rightindex] = message[leftindex]
        message[leftindex] = tempchar

        leftindex += 1
        rightindex -= 1

def reversewords(message):
    leftIndex = 0
    rightIndex = len(message)
    tempLetter = ''

    if len(message) <= 1 or ' ' not in message:
        return message

    # single pass to reverse all characters
    message.reverse()

    leftIndex = 0
    # while there are more spaces
    while True:
        if ' ' in message[leftIndex:]:
            nextSpace = message.index(' ', leftIndex)
            rightIndex = nextSpace - 1
        else:
            break

        # reverse the word
        reversechars(leftIndex, rightIndex, message)
        leftIndex = nextSpace + 1

    # reverse the last word
    rightIndex = len(message) - 1
    reversechars(leftIndex, rightIndex, message)

    return message


# Testing
message = ['c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l']

reversewords(message)
print(message)
