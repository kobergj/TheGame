import visualization.universe as uvs


def planetArrival(Planet, Player):
    print "==" * 20
    print "\n You are at Planet %s" % Planet.name
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
        choice = uvs.invalidChoice(choice)

    return choice


def chooseGoodToBuy(Planet, Player):
    i = 1
    print '\n Possiblities:'
    print "[0] Buy Nothing"
    for good in Planet.goodsProduced:
        print "[%s] buy %s for %s credits" % (i, good, Planet.prices[good])
        i += 1

    choice = input()

    while choice not in range(i):
        choice = uvs.invalidChoice(choice)

    if choice == 0:
        return 'quitBuy', 0

    good_to_buy = Planet.goodsProduced[choice-1]

    print "\n Choose Amount [0 - %s]:" % Player.currentShip.freeCargoSpace

    amount = input()

    while amount not in range(Player.currentShip.freeCargoSpace+1):
        amount = uvs.invalidChoice(amount)

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
        choice = uvs.invalidChoice(choice)

    if choice == 0:
        return 'quitSell', 0

    good_to_sell = choiceOptions[choice-1]

    print "\n Choose Amount [0-%s]:" % Player.currentShip.inCargo[good_to_sell]

    amount = input()

    while amount not in range(Player.currentShip.inCargo[good_to_sell]+1):
        amount = uvs.invalidChoice(amount)

    return good_to_sell, amount
