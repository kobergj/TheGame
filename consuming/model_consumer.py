import logbook.configuration as log

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
        log.log('Get Anomaly')
        anomaly = Universe[Player.currentPosition]

        log.log('Update Universe')
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
                log.log('Await Interaction Flag')
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

## TESTING TEMPLATE ##

class mainGame:

    def __init__(self):
        pass

    def logic(self, Universe, Player):

        atAnomaly = False

        while not atAnomaly:
            atAnomaly = self.UniverseScreen(Universe, Player)

            anomaly = Universe[Player.currentPosition]

        self.TravelScreen(anomaly, Player)

        while anomaly.enemies:
            try: self.EnemyScreen(anomaly, Player)
            except log.FleeError: atAnomaly = False 

        while atAnomaly:
            try: self.AnomalyScreen(anomaly, Player)
            except log.DepartError: atAnomaly = False


    def TravelScreen(self, Anomaly, Player):
        """No "Screen" at the moment :) 
            Player travels to Anomaly"""
        # Calc Travel Cost
        costForTravel = calculateTravelCosts(Player, Anomaly.coordinates)
        # Pay
        Player.spendCredits(costForTravel)
        # Travel
        Player.travelTo(Anomaly.coordinates)

        # Demock Stats
        Player.currentShip.maxTravelDistance.demock()
        Player.currentShip.maintenanceCosts.demock()


    def AnomalyScreen(self, Anomaly, Player):
        """One Interaction with an Anomaly.
            Raises DepartError if Player wants to depart"""
        # You get repaired When you land
        Player.currentShip.shieldStrength.reset()

        log.log('Get List of Available Sections')
        availableSections = ac.getAvailableSections(Anomaly, Player)

        log.log('Choose Section to Interact with')
        section = av.chooseSection(Anomaly, Player, availableSections)

        # Go to Section
        atSection = True

        while atSection:
            log.log('Choose Details for Interaction with %s' % str(section))
            sectionCallArgument = av.chooseInteraction(Anomaly, Player, section, atSection)

            log.log('Execute with args %s' % str(sectionCallArgument))
            atSection = section(Anomaly, Player, sectionCallArgument)

            # Reinitialize Section
            try: section.__init__(Anomaly, Player)
            except AttributeError: atSection = False


    def EnemyScreen(self, Anomaly, Player):
        """Enters the Enemy Screen. Raises an FleeError if Player flees"""
        # Get Enemy
        enemy = Anomaly.enemies[0]

        log.log('begin Fight')
        won = emy.beginFight(Player.currentShip, enemy)

        # Check For Sucess
        if not won:
            # Enemy Gets repaired
            enemy.shieldStrength.reset()

            log.log('Player flew')
            raise log.FleeError

        # Get Credits
        Player.earnCredits(enemy.lootableCredits)

        # Loot Wreck
        for good, amount in enemy.inCargo.iteritems():
            Player.currentShip.loadCargo(good, amount)

        log.log('Fight won. Killing Enemy')
        Anomaly.enemies.remove(enemy)


    def UniverseScreen(self, Universe, Player, home=False):
        """Show Universe Screen. Uses next Available Cords except home.
            Returns True if Player wants to Travel/Land, None else."""
        if home:
            # Start at Current Anomaly
            Universe.coCursor = [Player.currentPosition[0]-1, Player.currentPosition[1]]

        # Get a Anomaly
        anomaly = Universe.next(infinity=True)
        # Calc Price
        costForTravel = calculateTravelCosts(Player, anomaly.coordinates)
        # Reachable?
        if costForTravel is not None:
            log.log('Await Interaction Flag')
            travel = uv.chooseNextDestination(Universe, Player, anomaly.coordinates)
            return travel





class calculation:

    def calculateDistance(point1, point2):
        distance = 0.0
        for i in range(len(point1)):
            x = point1[i]
            y = point2[i]

            distance += (x - y)**2

        distance = math.sqrt(distance)
        distance = round(distance, 2)

        return distance

    def calculateTravelCosts(Player, Coordinates):
        # Get Distance
        distance = calculateDistance(Player.currentPosition, Coordinates)

        # Check if reachable
        if distance <= Player.currentShip.maxTravelDistance():
            # Calculate Costs
            travelCosts = int(distance * Player.currentShip.maintenanceCosts())

            return travelCosts
