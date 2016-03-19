
import consuming.controller.anomaly_controls as ac
import consuming.controller.enemy_interactions as emy

import consuming.visualization.anomaly_viz as av
import consuming.visualization.universe as uv

import math


def fillUniverse(Universe, NumberOfAnomalies):

    for i in range(NumberOfAnomalies):
        # Get Anomaly
        anomaly = Universe.anomalyQ.get()
        # Add Anomaly
        Universe.addAnomaly(anomaly)

class AnomalyInteraction():
    def __init__(self, Universe, Player):
        # Get Anomaly
        anomaly = Universe[Player.currentPosition]
        # Update Anomaly
        anomaly.update(Universe)

        # Interact Flag
        self.interact = False
        # Next Destination Coordinates
        self.departFromAnomaly = False

        # Start at Current Anomaly
        Universe.coCursor = [Player.currentPosition[0]-1, Player.currentPosition[1]]

        while not self.interact:
            # Get a Anomaly
            anomaly = Universe.next(infinity=True)
            # Calc Price
            costForTravel = calculateTravelCosts(Player, anomaly.coordinates)
            # Reachable?
            if costForTravel is not None:
                # Await choice
                self.interact = uv.chooseNextDestination(Universe, Player, anomaly.coordinates)

        # Want to Land?
        if anomaly.coordinates == Player.currentPosition:
            # Fight Enemies First
            while anomaly.enemies:
                # Get Enemy
                enemy = anomaly.enemies.pop(0)
                # Fight
                self.fight(enemy, Player)

            # Interact with Anomaly
            while not self.departFromAnomaly:
                # Land At Anomaly
                self.departFromAnomaly = self.land(anomaly, Player)

        # Depart
        self.depart(anomaly, Player)


    def fight(self, Enemy, Player):
        # Begin Fight
        emy.beginFight(Player.currentShip, Enemy)

    def land(self, Anomaly, Player):
        # Get List of Available Sections
        availableSections = ac.getAvailableSections(Anomaly, Player)
        # Choose Section to Interact with
        section = av.chooseSection(Anomaly, Player, availableSections)

        # Are there Iteractions?
        if len(section) != 0:
            # Go to Section
            atSection = True

            while atSection:
                # Get Details for Interaction
                sectionCallArgument = av.chooseInteraction(Anomaly, Player, section, atSection)

                # Execute
                atSection = section(Anomaly, Player, sectionCallArgument)

            return

        else:
            section(Anomaly, Player)
            return True


    def depart(self, Anomaly, Player):
        Player.travelTo(Anomaly.coordinates)


def calculateTravelCosts(Player, Coordinates):
    # Get Distance
    distance = calculateDistance(Player.currentPosition, Coordinates)

    # Check if reachable
    if distance <= Player.currentShip.maxTravelDistance():
        # Calculate Costs
        travelCosts = int(distance * Player.currentShip.maintenanceCosts())

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
