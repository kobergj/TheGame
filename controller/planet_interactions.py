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

    choice = viz.chooseNextDestination(Planet, Player)

    next_dest = Planet.distances.keys()[choice]

    return next_dest


def BuyGoods(Planet, Player):
    choice = viz.chooseGoodToBuy(Planet, Player)

    if choice == -1:
        return

    good_to_buy = Planet.goodsProduced[choice]
    price = Planet.prices[good_to_buy]

    Player.spendCredits(price)
    # TODO: CargoAmount
    Player.currentShip.loadCargo(good_to_buy, 1)


def SellGoods(Planet, Player):
    choice = viz.chooseGoodToSell(Planet, Player)

    if choice == -1:
        return

    good_to_sell = Player.currentShip.inCargo.keys()[choice]
    price = Planet.prices[good_to_sell]

    # TODO: CargoAmount
    Player.currentShip.unloadCargo(good_to_sell, 1)

    Player.earnCredits(price)
