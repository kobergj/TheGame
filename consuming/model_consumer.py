import logbook.configuration as log

import consuming.controller.anomaly_controls as ac
import consuming.controller.enemy_interactions as emy

import consuming.visualization.anomaly_viz as av
import consuming.visualization.universe as uv

import math


class Journey:

    def __init__(self, Universe, Player, StartingAnomaly, NumberOfAnomalies):
        # Add Starting Anomaly
        Universe.addAnomaly(StartingAnomaly)

        # Fill Universe
        self.fillUniverse(Universe, NumberOfAnomalies)

        # Power Engines
        Player.travelTo(StartingAnomaly.coordinates)

        log.log('Update Universe')
        Universe.update()

    def __call__(self, Universe, Player):
        anomaly = Universe[Player.currentPosition]

        first = True

        while not Player.atAnomaly:
            log.log('Loading Universe Screen')
            anomaly, travel = self.BrowseMap(Universe, Player, anomaly, first)
            first = False

            if travel:
                log.log('Traveling to %(name)s' % anomaly.__dict__)
                self.Travel(anomaly, Player)
                log.log('Update Universe')
                Universe.update()
                first = True

        while anomaly.enemies:
            log.log('Loading Enemy Screen')
            flee = self.Fight(anomaly, Player)
            if flee:
                Player.depart()
                break

        while Player.atAnomaly:
            log.log('Loading Anomaly Screen')
            self.Interact(anomaly, Player)


    def Travel(self, Anomaly, Player):
        """No "Screen" at the moment :) 
            Player travels to Anomaly. Returns True if Player wants to land"""
        # Get Distance
        Distance = self.calculateDistance(Player.currentPosition, Anomaly.coordinates)
        # Is current?
        if Distance == 0:
            Player.land()
            return

        # Calc Travel Cost
        costForTravel = self.calculateTravelCosts(Player, Distance)
        # Pay
        Player.spendCredits(costForTravel)
        # Travel
        Player.travelTo(Anomaly.coordinates)

        # Demock Stats
        Player.currentShip.maxTravelDistance.demock()
        Player.currentShip.maintenanceCosts.demock()


    def Interact(self, Anomaly, Player):
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

        if len(section) == 0:
            atSection = False
            section(Anomaly, Player)

        while atSection:
            log.log('Choose Details for Interaction with %s' % str(section))
            sectionCallArgument = av.chooseInteraction(Anomaly, Player, section, atSection)

            log.log('Execute with args %s' % str(sectionCallArgument))
            atSection = section(Anomaly, Player, sectionCallArgument)

            # Reinitialize Section
            try: section.__init__(Anomaly, Player)
            except AttributeError: atSection = False


    def Fight(self, Anomaly, Player):
        """Enters the Enemy Screen. Returns True if Player wants to flee"""
        # Get Enemy
        enemy = Anomaly.enemies[0]

        log.log('begin Fight')
        won = emy.beginFight(Player.currentShip, enemy)

        # Check For Sucess
        if not won:
            # Enemy Gets repaired
            enemy.shieldStrength.reset()

            log.log('Player flew')
            return True

        # Get Credits
        Player.earnCredits(enemy.lootableCredits)

        # Loot Wreck
        for good, amount in enemy.inCargo.iteritems():
            Player.currentShip.loadCargo(good, amount)

        log.log('Fight won. Killing Enemy')
        Anomaly.enemies.remove(enemy)


    def BrowseMap(self, Universe, Player, ActiveAnomaly, first=False):
        """Show Universe Screen. Uses next Available Cords except home.
            Returns True if Player wants to Travel/Land, None else."""
        ActiveCoordinates = ActiveAnomaly.coordinates[:]

        if first:
            # Start at Current Anomaly
            ActiveCoordinates = [ActiveCoordinates[0]-1, ActiveCoordinates[1]]

        log.log('Getting next Anomaly from %s' % ActiveCoordinates)
        anomaly = Universe.next(infinity=True, start=ActiveCoordinates)

        log.log('Calculate Travel Costs to %(name)s' % anomaly.__dict__)
        distance = self.calculateDistance(Player.currentPosition, anomaly.coordinates)
        costForTravel = self.calculateTravelCosts(Player, distance)

        # Reachable?
        if costForTravel is not None:
            log.log('Await Interaction Flag')
            travel = uv.chooseNextDestination(Universe, Player, anomaly.coordinates, costForTravel)
            return anomaly, travel

        return anomaly, False

    def calculateDistance(self, point1, point2):
        distance = 0.0
        for i in range(len(point1)):
            x = point1[i]
            y = point2[i]

            distance += (x - y)**2

        distance = math.sqrt(distance)
        distance = round(distance, 2)

        return distance

    def calculateTravelCosts(self, Player, Distance):
        # Check if reachable
        if Distance <= Player.currentShip.maxTravelDistance():
            # Calculate Costs
            travelCosts = int(Distance * Player.currentShip.maintenanceCosts())

            return travelCosts

    def fillUniverse(self, Universe, NumberOfAnomalies):

        for i in range(NumberOfAnomalies):
            # Get Anomaly
            anomaly = Universe.anomalyQ.get()
            # Add Anomaly
            Universe.addAnomaly(anomaly)
