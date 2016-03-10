import consuming.visualization.universe as viz


def ChooseDestination(Universe, Player):
    next_dest = viz.chooseNextDestination(Universe, Player)

    if next_dest:
        print next_dest
        # Calculate Costs
        cost_for_travel = Player.currentShip.travelCosts[next_dest]
        # Pay the Price
        Player.spendCredits(cost_for_travel)
        # Travel to Next Destination
        Player.travelTo(next_dest)

        return

    return True
