import consuming.visualization.universe as viz


def ChooseDestination(Universe, Player):
    next_dest_coordinates = viz.chooseNextDestination(Universe, Player)

    if next_dest_coordinates:
        next_anomaly = Universe.callAnomaly(next_dest_coordinates)
        # Calculate Costs
        cost_for_travel = Player.currentShip.travelCosts[next_anomaly.name]
        # Pay the Price
        Player.spendCredits(cost_for_travel)
        # Travel to Next Destination
        Player.travelTo(next_anomaly.coordinates)

        return

    return True
