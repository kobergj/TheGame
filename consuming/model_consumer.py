
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

    # First Update
    # Universe.update(Universe)

class AnomalyInteraction():
    def __init__(self, Universe, Player):
        # Get Anomaly
        anomaly = Universe[Player.currentPosition]

        # Update
        Universe.update()

        # Interact Flag
        self.interact = False
        # Next Destination Coordinates
        self.departFromAnomaly = False

        # Start at Current Anomaly
        Universe.coCursor = [Player.currentPosition[0]-1, Player.currentPosition[1]]

        # Choose what to do next
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

            # Interact with Anomaly
            while not self.departFromAnomaly:
                # Land At Anomaly
                try:
                    self.departFromAnomaly = self.land(anomaly, Player)
                except FleeError:
                    self.departFromAnomaly = True
        else:
            # Depart
            self.depart(anomaly, Player)


    def fight(self, Enemy, Player):
        # Begin Fight
        won = emy.beginFight(Player.currentShip, Enemy)

        return won

    def land(self, Anomaly, Player):
        # Fight Enemies First
        while Anomaly.enemies:
            # Get Enemy
            enemy = Anomaly.enemies[0]
            # Fight
            won = self.fight(enemy, Player)
            # Check For Sucess
            if not won:
                # Enemy Gets repaired
                enemy.shieldStrength.reset()
                raise FleeError

            # Get Credits
            Player.earnCredits(enemy.lootableCredits)
            # Loot Wreck
            for good, amount in enemy.inCargo.iteritems():
                Player.currentShip.loadCargo(good, amount)
            # Kill Enemy
            Anomaly.enemies.remove(enemy)

        # You get repaired When you land
        Player.currentShip.shieldStrength.reset()

        # Get List of Available Sections
        availableSections = ac.getAvailableSections(Anomaly, Player)
        # Choose Section to Interact with
        section = av.chooseSection(Anomaly, Player, availableSections)

        # Are there any further Interactions?
        if len(section) != 0:
            # Go to Section
            atSection = True

            while atSection:
                # Get Details for Interaction
                sectionCallArgument = av.chooseInteraction(Anomaly, Player, section, atSection)

                # Execute
                atSection = section(Anomaly, Player, sectionCallArgument)

                # Reinitialize Section
                try: section.__init__(Anomaly, Player)
                except AttributeError: atSection = False

            return

        else:
            section(Anomaly, Player)
            return True


    def depart(self, Anomaly, Player):
        # Calc Travel Cost
        costForTravel = calculateTravelCosts(Player, Anomaly.coordinates)
        # Pay
        Player.spendCredits(costForTravel)
        # Travel
        Player.travelTo(Anomaly.coordinates)

        # Demock Stats
        Player.currentShip.maxTravelDistance.demock()
        Player.currentShip.maintenanceCosts.demock()



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

class FleeError(Exception):
    pass
