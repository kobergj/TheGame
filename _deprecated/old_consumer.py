import logging

import consuming.controller.anomaly_controls as ac
import consuming.controller.enemy_interactions as emy

import consuming.visualization.terminal_viz as term

class Journey:


    def __call__(self, Universe, Player):
        anomaly = Universe[Player.currentPosition]

        first = True

        anomaly = Universe[Player.currentPosition]

        while not Player.atAnomaly:
            logging.info('Loading Universe Screen')
            anomaly, land = self.BrowseMap(Universe, Player, anomaly, first)
            first = False

            

        # while anomaly.enemies:
        #     logging.info('Loading Enemy Screen')
        #     flee = self.Fight(anomaly, Player)
        #     if flee:
        #         Player.depart()
        #         break

        while Player.atAnomaly:
            logging.info('Loading Anomaly Screen')
            self.Interact(Universe, Player)

        Universe.update(Player)




    def Interact(self, Universe, Player):
        """One Interaction with an Anomaly."""
        Anomaly = Universe[Player.currentPosition]

        # You get repaired When you land
        Player.currentShip.shieldStrength.reset()

        logging.info('Get List of Available Sections')
        availableSections = ac.getAvailableSections(Anomaly, Player)

        logging.info('Init Anomaly %s' % Anomaly.coordinates)
        view = term.AnomalyView(Universe, Player, availableSections)

        logging.info('Choose Section to Interact with')
        section = view()

        try: section(Anomaly, Player)
        except TypeError:
            atSection = True
            while atSection:
                logging.info('Init Section %s' % section.infoString())
                view = term.SectionView(Universe, Player, section)

                logging.info('Choose Interaction')
                argument = view()

                logging.info('Execute Interaction')
                atSection = section(Anomaly, Player, argument)

    def Fight(self, Anomaly, Player):
        """Enters the Enemy Screen. Returns True if Player wants to flee"""
        # Get Enemy
        enemy = Anomaly.enemies[0]

        logging.info('begin Fight')
        won = emy.beginFight(Player.currentShip, enemy)

        # Check For Sucess
        if not won:
            # Enemy Gets repaired
            enemy.shieldStrength.reset()

            logging.info('Player flew')
            return True

        # Get Credits
        Player.earnCredits(enemy.lootableCredits)

        # Loot Wreck
        for good, amount in enemy.inCargo.iteritems():
            Player.currentShip.loadCargo(good, amount)

        logging.info('Fight won. Killing Enemy')
        Anomaly.enemies.remove(enemy)


    def BrowseMap(self, Universe, Player, ActiveAnomaly, first=False):
        """Show Universe Screen. Uses next Available Cords except first is given.
            Returns True if Player wants to Travel/Land, None else."""

        ActiveCoordinates = ActiveAnomaly.coordinates[:]

        if first:
            # Start at Current Anomaly
            ActiveCoordinates = [ActiveCoordinates[0]-1, ActiveCoordinates[1]]

        logging.info('Getting next Anomaly from %s' % ActiveCoordinates)
        anomaly = Universe.next(infinity=True, start=ActiveCoordinates)

        # Reachable?
        if anomaly.travelCosts is not None:
            logging.info('Await Interaction with %s' % anomaly.coordinates)
            view = term.UniverseView(Universe, Player, anomaly)

            interact = view()

            if interact:
                return anomaly, True

        return anomaly, False
