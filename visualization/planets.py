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


def chooseNextDestination(Planet, Player):
    # Returns Index of Destination in Planet.distances.keys()
    print "\n Choose Destination"

    i = 1
    for destination in Planet.distances.keys():
        print "[%s] %s, distance: %s clicks" % (i, destination, Planet.distances[destination])
        i += 1

    choice = input()

    while choice not in range(i):
        choice = invalidChoice(choice)

    return choice - 1


def chooseGoodToBuy(Planet, Player):
    # Returns Index of Good in Planet.goodsProduced or -1 for quit
    i = 1
    print '\n Possiblities:'
    print "[0] Buy Nothing"
    for good in Planet.goodsProduced:
        print "[%s] buy %s for %s credits" % (i, good, Planet.prices[good])
        i += 1

    choice = input()

    while choice not in range(i):
        choice = invalidChoice(choice)

    return choice - 1


def chooseGoodToSell(Planet, Player):
    # Returns Index of Good in Player.currentShip.inCargo.keys() or -1 for quit
    i = 1
    print '\n Possiblities:'
    print "[0] sell Nothing"
    for good in Player.currentShip.inCargo.keys():
        if good in Planet.goodsConsumed:
            print "[%s] sell %s for %s credits" % (i, good, Planet.prices[good])
            i += 1

    choice = input()

    while choice not in range(i):
        choice = invalidChoice(choice)

    return choice - 1
