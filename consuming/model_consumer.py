import logbook.configuration as log

import consuming.controller.anomaly_controls as ac
import consuming.controller.enemy_interactions as emy

import consuming.visualization.terminal_viz as term

class Journey:

    def __init__(self, Universe, Player, StartingAnomaly, NumberOfAnomalies):
        # Add Starting Anomaly
        Universe.addAnomaly(StartingAnomaly)

        # Fill Universe
        self.fillUniverse(Universe, NumberOfAnomalies)

        # Power Engines
        Player.travelTo(StartingAnomaly.coordinates)

        log.log('Update Universe')
        Universe.update(Player)

    def __call__(self, Universe, Player):
        anomaly = Universe[Player.currentPosition]

        first = True

        anomaly = Universe[Player.currentPosition]

        while not Player.atAnomaly:
            log.log('Loading Universe Screen')
            anomaly, land = self.BrowseMap(Universe, Player, anomaly, first)
            first = False

            if land:
                log.log('Execute Travel Logic')
                self.Travel(anomaly, Player)
                log.log('Update Universe')
                Universe.update(Player)
                first = True

        # while anomaly.enemies:
        #     log.log('Loading Enemy Screen')
        #     flee = self.Fight(anomaly, Player)
        #     if flee:
        #         Player.depart()
        #         break

        while Player.atAnomaly:
            log.log('Loading Anomaly Screen')
            self.Interact(Universe, Player)

        Universe.update(Player)


    def Travel(self, Anomaly, Player):
        """No "Screen" at the moment :) 
            Player travels to Anomaly. Returns True if Player wants to land"""

        if Anomaly.travelCosts is None:
            return

        # Is current?
        if Anomaly.coordinates == Player.currentPosition:
            log.log('%(name)s is current. Landing...' % Anomaly.__dict__)
            Player.land()
            return

        log.log('Pay Costs of %(travelCosts)s' % Anomaly.__dict__)
        Player.spendCredits(Anomaly.travelCosts)
        log.log('Traveling to %(name)s' % Anomaly.__dict__)
        Player.travelTo(Anomaly.coordinates)

        # Demock Stats
        Player.currentShip.maxTravelDistance.demock()
        Player.currentShip.maintenanceCosts.demock()


    def Interact(self, Universe, Player):
        """One Interaction with an Anomaly."""
        Anomaly = Universe[Player.currentPosition]

        sectionScreen = term.MainScreen(Universe, Player)

        # You get repaired When you land
        Player.currentShip.shieldStrength.reset()

        log.log('Get List of Available Sections')
        availableSections = ac.getAvailableSections(Anomaly, Player)

        log.log('Choose Section to Interact with')
        # section = av.chooseSection(Anomaly, Player, availableSections, MapTemplate)
        section = sectionScreen(Player, avail_secs=availableSections)

        try: section(Anomaly, Player)
        except TypeError:
            atSection = True
            while atSection:
                # ReInit sectionScreen
                sectionScreen.__init__(Universe, Player)

                log.log('Choose Interaction')
                argument = sectionScreen(Player, active_sec=section)

                atSection = section(Anomaly, Player, argument)

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
        """Show Universe Screen. Uses next Available Cords except first is given.
            Returns True if Player wants to Travel/Land, None else."""
        mainScreen = term.MainScreen(Universe, Player)

        ActiveCoordinates = ActiveAnomaly.coordinates[:]

        if first:
            # Start at Current Anomaly
            ActiveCoordinates = [ActiveCoordinates[0]-1, ActiveCoordinates[1]]

        log.log('Getting next Anomaly from %s' % ActiveCoordinates)
        anomaly = Universe.next(infinity=True, start=ActiveCoordinates)

        # log.log('Calculate Travel Costs to %(name)s' % anomaly.__dict__)
        # distance = self.calculateDistance(Player.currentPosition, anomaly.coordinates)
        # costForTravel = self.calculateTravelCosts(Player, distance)

        # Reachable?
        if anomaly.travelCosts is not None:
            log.log('Await Interaction with %s' % anomaly.coordinates)
            interact = mainScreen(Player, active_anmy=anomaly)

            if interact:
                return anomaly, True

        return anomaly, False


    def fillUniverse(self, Universe, NumberOfAnomalies):

        for i in range(NumberOfAnomalies):
            # Get Anomaly
            anomaly = Universe.anomalyQ.get()
            # Add Anomaly
            Universe.addAnomaly(anomaly)
