import consuming.visualization.universe as viz
import math


def ChooseDestination(Universe, Player):
    # Set Current Position
    activeCoordinates = Player.currentPosition
    # Init get anomaly function
    getAnomaly = Universe.callAnomaly
    # Choose Next
    while activeCoordinates:
        # Call Anomaly
        anomaly = getAnomaly(activeCoordinates)
        # Reassign Active Coordinates
        activeCoordinates = anomaly.coordinates
        # Calculate Costs
        costForTravel = calculateTravelCosts(Player, anomaly)
        # Reachable?
        if costForTravel:
            # Reassign Get Anomaly Func
            getAnomaly = viz.chooseNextDestination(Universe, Player, activeCoordinates, costForTravel)

    # Wanna Land?
    if anomaly.coordinates == Player.currentPosition:
        return True

    # Pay the Price
    Player.spendCredits(costForTravel)
    # Travel to Next Destination
    Player.travelTo(anomaly.coordinates)

    return


def calculateTravelCosts(Player, Anomaly):
    # Get Distance
    distance = calculateDistance(Player.currentPosition, Anomaly.coordinates)

    # Check if reachable
    if distance <= Player.currentShip.maxTravelDistance:
        # Calculate Costs
        travelCosts = int(distance * Player.currentShip.maintenanceCosts)

        return travelCosts


def calculateDistance(point1, point2):
    distance = 0.0
    for i in range(len(point1)):
        x = point1[i]
        y = point2[i]

        distance += (x - y)**2

    distance = math.sqrt(distance)
    distance = round(distance, 2)

    return distance
