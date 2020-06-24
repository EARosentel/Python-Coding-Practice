def sortscores(maxscore, scores):
    scorearray = [0]*maxscore

    for score in scores:
        scorearray[score] += 1

    counter = maxscore - 1
    while counter > -1:
        if scorearray[counter] > 0:
            return counter
        else:
            counter -= 1

    return 0


# testing
maxscore1 = 100
maxscore2 = 1000

scores1 = [1,3,70,65,39,97,-55,23]
scores2 = [200,300,100,700,797,823,521,1]

print(sortscores(maxscore1,scores1))
print(sortscores(maxscore2,scores2))
