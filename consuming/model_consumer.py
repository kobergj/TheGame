import consuming.controller.planet_interactions as pi
import consuming.controller.spacegate_interactions as sgi
import consuming.controller.starbase_interactions as sbi
import consuming.controller.enemy_interactions as emy
import consuming.controller.universe_interactions as ui


LOCATION_OF_ARRIVING_FUNCS = {
    'Planet': pi.Arrive,
    'Starbase': sbi.Arrive,
    'Spacegate': sgi.Arrive,
}


def fillUniverse(Universe, NumberOfAnomalies):

    for i in range(NumberOfAnomalies):
        # Get Anomaly
        anomaly = Universe.anomalyQ.get()
        # Add Anomaly
        Universe.addAnomaly(anomaly)


def arriveAtAnomaly(Player, Universe):
    # Get Anomaly
    anomaly = Universe.callAnomaly(Player.currentPosition)
    # Update Anomaly
    anomaly.update(Universe)

    # get Distance Dict
    distanceDict = Universe.generateDistanceDict(anomaly.coordinates)
    # Scan Sector
    Player.currentShip.scanSector(distanceDict)

    # Choose Next Destination
    interact_with_anomaly = ui.ChooseDestination(Universe, Player)

    # start Anomaly Interaction
    while interact_with_anomaly:
        # Fight ALL Enemies First
        while anomaly.enemies:
            # Get Enemy
            enemy = anomaly.enemies[0]
            # Begin Fight
            won = emy.beginFight(Player.currentShip, enemy)
            # Check For Winner
            if won:
                # Kill Enemy
                anomaly.enemies.remove(enemy)
            # Choose next Destination
            interact_with_anomaly = ui.ChooseDestination(Universe, Player)
            # Check For Landing Sequence
            if not interact_with_anomaly:
                return

        # Get Anomaly Class
        anomalyClass = anomaly.__class__.__name__
        # Get Arriving Func
        arrive = LOCATION_OF_ARRIVING_FUNCS[anomalyClass]
        # Arrive
        arrive(anomaly, Player)

        # Choose Next Destination
        interact_with_anomaly = ui.ChooseDestination(Universe, Player)
