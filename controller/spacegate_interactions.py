
def Arrive(Spacegate, Player):
    # Pay Fee
    Player.spendCredits(Spacegate.costForUse)

    # Override travelcosts
    Player.currentShip.travelCosts = Spacegate.travelCostDict

    return
