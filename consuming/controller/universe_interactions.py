import consuming.visualization.universe as viz
import math


def chooseInteractionType(Universe, Player):
    # Assign coordinates
    coordinates = Player.currentPosition
    # Init
    interact = viz.chooseNextDestination(Universe, Player)
    # Choose Next
    while not interact:
        interact, coordinates = loopThroughAnomalies(Universe, Player)

    # Load destination Anomaly
    anomaly = Universe[coordinates]

    # Wanna Land?
    if anomaly.coordinates == Player.currentPosition:
        return True

    # Calc Travel Costs
    costForTravel = calculateTravelCosts(Player, anomaly.coordinates)
    # Pay
    Player.spendCredits(costForTravel)
    # Travel to Next Destination
    Player.travelTo(anomaly.coordinates)


def loopThroughAnomalies(Universe, Player):
    # Get Anomaly
    anomaly = Universe.next(infinity=True)

    # Calculate Costs
    costForTravel = calculateTravelCosts(Player, anomaly.coordinates)

    # Reachable?
    if costForTravel is not None:
        # Choose next
        interact = viz.chooseNextDestination(Universe, Player, anomaly.coordinates, costForTravel)

        if interact:
            return interact, anomaly.coordinates

    return None, None


def calculateTravelCosts(Player, Coordinates):
    # Get Distance
    distance = calculateDistance(Player.currentPosition, Coordinates)

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
