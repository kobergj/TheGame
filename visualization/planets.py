
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

    choiceList = list()

    i = 1
    print "[0] Show Sector Map"
    for destination in Planet.distances.keys():
        if Planet.distances[destination] <= Player.currentShip.maxTravelDistance:
            print "[%s] %s, distance: %s clicks, Cost: %s" % (i,
                                                              destination,
                                                              Planet.distances[destination],
                                                              travelCosts[destination])
            i += 1
            choiceList.append(destination)

    choice = input()

    while choice not in range(i):
        choice = invalidChoice(choice)

    if choice == 0:
        showSectorMap(Player, Planet)

    next_dest = choiceList[choice-1]

    return next_dest


def showSectorMap(Planet, Player):
    

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

    print "\n Choose Amount [0 - %s]:" % Player.currentShip.freeCargoSpace

    amount = input()

    while amount not in range(Player.currentShip.freeCargoSpace+1):
        amount = invalidChoice(amount)

    return good_to_buy, amount


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

    print "\n Choose Amount [0-%s]:" % Player.currentShip.inCargo[good_to_sell]

    amount = input()

    while amount not in range(Player.currentShip.inCargo[good_to_sell]+1):
        amount = invalidChoice(amount)

    return good_to_sell, amount
