def getmaxprofit(stockprices):
    print('Pricelist: ')
    print(stockprices)
    maxprofit = 0
    currentprofit = 0
    lowestseen = stockprices[0]
    highestseen = stockprices[0]
    for x in range(len(stockprices)):
        if stockprices[x] > highestseen:
            highestseen = stockprices[x]
        elif stockprices[x] < lowestseen:
            lowestseen = stockprices[x]
            highestseen = lowestseen

        currentprofit = highestseen - lowestseen
        print('highest seen ',highestseen)
        print('lowest seen ',lowestseen)
        print('current profit ',currentprofit)

        if maxprofit < currentprofit:
            maxprofit = currentprofit
            print('new max profit: ',maxprofit)

    return maxprofit


# testing
stocks1 = [5,9,10,8,7,4,11]
stocks2 = [5,4,3,2,1]
stocks3 = [3,17,2,1,1,8]

print(getmaxprofit(stocks1))
print(getmaxprofit(stocks2))
print(getmaxprofit(stocks3))
