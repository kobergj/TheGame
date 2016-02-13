import visualization.planets as vizplnt
import visualization.universe as vizuvs


def Arrive(Planet, Player):
    while True:
        choice = vizplnt.planetArrival(Planet, Player)

        if choice == 0:
            return 'quit'

        elif choice == 1:
            BuyGoods(Planet, Player)

        elif choice == 2:
            SellGoods(Planet, Player)

        elif choice == 3:
            return

        else:
            choice = vizuvs.invalidChoice(choice)


def BuyGoods(Planet, Player):
    good_to_buy, amount = vizplnt.chooseGoodToBuy(Planet, Player)

    if good_to_buy == 'quitBuy':
        return

    if amount == 0:
        return

    price = Planet.prices[good_to_buy]

    Player.spendCredits(price*amount)

    Player.currentShip.loadCargo(good_to_buy, amount)


def SellGoods(Planet, Player):
    good_to_sell, amount = vizplnt.chooseGoodToSell(Planet, Player)

    if good_to_sell == 'quitSell':
        return

    if amount == 0:
        return

    price = Planet.prices[good_to_sell]

    Player.currentShip.unloadCargo(good_to_sell, amount)

    Player.earnCredits(price*amount)
