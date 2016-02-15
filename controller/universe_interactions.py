import visualization.universe as viz


def ChooseDestination(Universe, Player):
    next_dest = viz.chooseNextDestination(Universe, Player)

    if next_dest != 'land':
        cost_for_travel = Player.currentShip.travelCosts[next_dest]
        Player.spendCredits(cost_for_travel)

    return next_dest
