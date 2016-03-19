# import consuming.visualization.planets as vizplnt


# def Arrive(Planet, Player):
#     # generate List of Actions
#     possibleActions = {'quit': Quit,
#                        'buyGoods': BuyGoods,
#                        'sellGoods': SellGoods,
#                        'depart': Depart
#                        }

#     while True:
#         # Get Choice From Player
#         choice = vizplnt.planetArrival(Planet, Player)

#         # Execute Choice
#         killSwitch = possibleActions[choice](Planet, Player)

#         # Kill While Loop
#         if killSwitch:
#             return


# def Depart(Planet, Player):
#     return True


# def Quit(Planet, Player):
#     quit()


# def BuyGoods(Planet, Player):
#     good_to_buy, amount = vizplnt.chooseGoodToBuy(Planet, Player)

#     if good_to_buy == 'quitBuy':
#         return

#     if amount == 0:
#         return

#     price = Planet.prices[good_to_buy]

#     Player.spendCredits(price*amount)

#     Player.currentShip.loadCargo(good_to_buy, amount)


# def SellGoods(Planet, Player):
#     good_to_sell, amount = vizplnt.chooseGoodToSell(Planet, Player)

#     if good_to_sell == 'quitSell':
#         return

#     if amount == 0:
#         return

#     price = Planet.prices[good_to_sell]

#     Player.currentShip.unloadCargo(good_to_sell, amount)

#     Player.earnCredits(price*amount)
