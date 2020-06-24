def wordcloud(sentence):
    wordset = {}
    words = sentence.split()

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for word in words:
        word = word.lower()
        if word[len(word)-1] not in alphabet:
            word = word[0:len(word)-1]
        if word in wordset:
            count = wordset[word]
            wordset[word] = count+1
        else:
            wordset[word] = 1

    return wordset


# testing
sentence1 = "After beating the eggs, Dana read the next step:"
sentence2 = "Can can can you do the can-can"
sentence3 = "Will Will will it?"
sentence4 = "To die. To sleep. Yes, to sleep. " \
            "Perchance to dream. Ah, there's the rub. " \
            "For in that sleep what dreams may come."

print(wordcloud(sentence1))
print(wordcloud(sentence2))
print(wordcloud(sentence3))
print(wordcloud(sentence4))
