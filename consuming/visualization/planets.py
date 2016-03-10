import consuming.visualization.universe as uvs


def planetArrival(Planet, Player):
    # Initialize Print String
    to_print = ''

    # Flush Terminal
    to_print += '\n' * 100

    # Fancy Border
    to_print += "==" * 40

    # Planet Informations
    to_print += "\n You are at Planet %s" % Planet.name
    to_print += "\nGoods Produced: %s" % Planet.goodsProduced
    to_print += "\nGoods Consumed: %s" % Planet.goodsConsumed

    # Player Informations
    to_print += "\n\nCurrently in Cargobay: %s" % Player.currentShip.inCargo
    to_print += "\nNumber of Credits: %s" % Player.credits

    # Possible Actions
    to_print += "\nPossible Actions:"

    choiceList = list()

    to_print += "\n[0] Quit Game"
    choiceList.append('quit')

    to_print += "\n[1] Buy Goods"
    choiceList.append('buyGoods')

    to_print += "\n[2] Sell Goods"
    choiceList.append('sellGoods')

    to_print += "\n[3] Depart"
    choiceList.append('depart')

    # Print String
    print to_print

    # Await Players Choice
    choice = input()

    while choice not in range(4):
        choice = uvs.invalidChoice(choice)

    choice = choiceList[choice]

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
