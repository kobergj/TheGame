
def Arrive(Spacegate, Player):
    # Generate travel cost dict
    travelCostDict = dict()
    for dest in Player.currentShip.travelCosts:
        travelCostDict.update({dest: Spacegate.costForUse})

    # Override travelcosts
    Player.currentShip.travelCosts = travelCostDict

    return
