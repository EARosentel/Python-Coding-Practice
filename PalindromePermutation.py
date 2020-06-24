def palindromepermutation(word):
    letters = set()
    for letter in word:
        if letter in letters:
            letters.remove(letter)
        else:
            letters.add(letter)

    if len(letters) > 1:
        return False
    else:
        return True


# testing
word1 = "civic"
word2 = "cciiv"
word3 = "aaaaa"
word4 = "abbb"
word5 = "palindrome"

print(palindromepermutation(word1))
print(palindromepermutation(word2))
print(palindromepermutation(word3))
print(palindromepermutation(word4))
print(palindromepermutation(word5))
