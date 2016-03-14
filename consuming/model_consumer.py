import consuming.controller.planet_interactions as pi
import consuming.controller.spacegate_interactions as sgi
import consuming.controller.starbase_interactions as sbi
import consuming.controller.enemy_interactions as emy
import consuming.controller.universe_interactions as ui

import consuming.controller.anomaly_controls as ac
import consuming.visualization.anomaly_viz as av


LOCATION_OF_ARRIVING_FUNCS = {
    'Planet':       pi.Arrive,
    'Starbase':     sbi.Arrive,
    'Spacegate':    sgi.Arrive,
}

LOCATION_OF_DEPARTING_FUNCS = {
    'Planet':       pi.Depart,
    'Starbase':     sbi.Depart,
    'Spacegate':    sgi.Depart
}


def fillUniverse(Universe, NumberOfAnomalies):

    for i in range(NumberOfAnomalies):
        # Get Anomaly
        anomaly = Universe.anomalyQ.get()
        # Add Anomaly
        Universe.addAnomaly(anomaly)


def fightEnemy(Player, Universe):
    # Get Anomaly
    anomaly = Universe[Player.currentPosition]
    # Get Enemy
    enemy = anomaly.enemies[0]
    # Begin Fight
    won = emy.beginFight(Player.currentShip, enemy)
    # Check For Winner
    if won:
        # Kill Enemy
        anomaly.enemies.remove(enemy)
    # Still a chance to flee
    landAtAnomaly = ui.chooseInteractionType(Universe, Player)

    return landAtAnomaly


def landAtAnomaly(Player, Anomaly):
    # # Get Anomaly Class
    # anomalyClass = Anomaly.__class__.__name__
    # # Get Arriving Func
    # arrive = LOCATION_OF_ARRIVING_FUNCS[anomalyClass]
    # # Arrive
    # arrive(Anomaly, Player)

    # land
    atAnomaly = True

    while atAnomaly:
        # Get List of Available Sections
        availableSections = ac.getAvailableSections(Anomaly, Player)
        # Choose Section to Interact with
        section = av.chooseSection(Anomaly, Player, availableSections)

        if len(section) != 0:
            # Go to Section
            atSection = True

            while atSection:
                # Get Details for Interaction
                sectionCallArgument = av.chooseInteraction(Anomaly, Player, section)

                # Execute
                atSection = section(Anomaly, Player, sectionCallArgument)

        else:
            section(Anomaly, Player)

    return


def interactWithAnomaly(Player, Universe):
    # Get Anomaly
    anomaly = Universe[Player.currentPosition]
    # Update Anomaly
    anomaly.update(Universe)

    # Choose Next Destination
    land = ui.chooseInteractionType(Universe, Player)

    # Begin Landing Sequence
    while land and anomaly.enemies:
        land = fightEnemy(Player, Universe)

    if land and not anomaly.enemies:
        # Land
        landAtAnomaly(Player, anomaly)
        # Done Shopping?
        land = ui.chooseInteractionType(Universe, Player)
        # Extr Anomaly Class
        anomalyClass = anomaly.__class__.__name__
        # Get Depart Func
        depart = LOCATION_OF_DEPARTING_FUNCS[anomalyClass]
        # Depart
        depart(anomaly, Player)
