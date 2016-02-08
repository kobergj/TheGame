import visualization.planets as viz


def Arrive(Planet, Player):
    while True:
        choice = viz.planetArrival(Planet, Player)

        if choice == 0:
            return 'quit'

        elif choice == 1:
            BuyGoods(Planet, Player)

        elif choice == 2:
            SellGoods(Planet, Player)

        elif choice == 3:
            next_dest_name = ChooseDestination(Planet, Player)
            return next_dest_name

        else:
            choice = viz.invalidChoice(choice)


def ChooseDestination(Planet, Player):
    travelCostDict = dict()
    for destination in Planet.distances:
        travelCost = int(Planet.distances[destination] / Player.currentShip.speed)
        travelCostDict.update({destination: travelCost})

    next_dest = viz.chooseNextDestination(Planet, Player, travelCostDict)

    cost_for_travel = travelCostDict[next_dest]
    Player.spendCredits(cost_for_travel)

    return next_dest


def BuyGoods(Planet, Player):
    good_to_buy = viz.chooseGoodToBuy(Planet, Player)

    if good_to_buy == 'quitBuy':
        return

    price = Planet.prices[good_to_buy]

    Player.spendCredits(price)
    # TODO: CargoAmount
    Player.currentShip.loadCargo(good_to_buy, 1)


def SellGoods(Planet, Player):
    good_to_sell = viz.chooseGoodToSell(Planet, Player)

    if good_to_sell == 'quitSell':
        return

    price = Planet.prices[good_to_sell]

    # TODO: CargoAmount
    Player.currentShip.unloadCargo(good_to_sell, 1)

    Player.earnCredits(price)
