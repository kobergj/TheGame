def planetArrival(Planet, Player):
    print "\n You are at Planet %s" % Planet.Name
    print "Goods Produced: %s" % Planet.goodsProduced
    print "Goods Consumed: %s" % Planet.goodsConsumed
    print "\nCurrently in Cargobay: %s" % Player.currentShip.inCargo
    print "Number of Credits: %s" % Player.credits
    print "\nPossible Actions:"
    print "[0] quit game"
    print "[1] buy goods"
    print "[2] sell goods"
    print "[3] depart"

    choice = input()

    while choice not in range(4):
        choice = invalidChoice(choice)

    return choice


def invalidChoice(choice):
    print 'Sorry, %s not valid' % choice
    choice = input()

    return choice


def chooseNextDestination(Planet, Player, travelCosts):
    print "\n Choose Destination"

    i = 1
    for destination in Planet.distances.keys():
        print "[%s] %s, distance: %s clicks, Cost: %s" % (i, destination, Planet.distances[destination], travelCosts[destination])
        i += 1

    choice = input()

    while choice not in range(i):
        choice = invalidChoice(choice)

    next_dest = Planet.distances.keys()[choice-1]

    return next_dest


def drawSectorMap(universe):
    mapdict = dict()
    for anomalyName in universe.anomalyList:
        anomaly = universe.__dict__[anomalyName]

        mapdict.update{}


def chooseGoodToBuy(Planet, Player):
    i = 1
    print '\n Possiblities:'
    print "[0] Buy Nothing"
    for good in Planet.goodsProduced:
        print "[%s] buy %s for %s credits" % (i, good, Planet.prices[good])
        i += 1

    choice = input()

    while choice not in range(i):
        choice = invalidChoice(choice)

    if choice == 0:
        return 'quitBuy'

    good_to_buy = Planet.goodsProduced[choice-1]

    return good_to_buy


def chooseGoodToSell(Planet, Player):
    choiceOptions = list()

    i = 1
    print '\n Possiblities:'
    print "[0] sell Nothing"
    for good in Player.currentShip.inCargo.keys():
        if good in Planet.goodsConsumed:
            print "[%s] sell %s for %s credits" % (i, good, Planet.prices[good])
            choiceOptions.append(good)
            i += 1

    choice = input()

    while choice not in range(i):
        choice = invalidChoice(choice)

    if choice == 0:
        return 'quitSell'

    good_to_sell = Player.currentShip.inCargo.keys()[choice-1]

    return good_to_sell
