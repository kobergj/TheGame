import controller.planet_interactions as pi
import controller.spacegate_interactions as sgi
import controller.starbase_interactions as sbi
import controller.enemy_interactions as emy
import controller.universe_interactions as ui


def Arrive(Player, Universe):
    # Get Anomaly
    anomaly = Universe.anomalyList[Player.currentPosition]

    # scan Sector
    Universe.updateDistances(Player.currentShip, anomaly.coordinates)
    Player.currentShip.scanSector()

    # Get Enemy from Queue
    newEnemy = anomaly.enemyQ.get()
    # Append to Enemy List
    if newEnemy:
        anomaly.enemies.append(newEnemy)

    # Choose Next Destination
    interact_with_anomaly = ui.ChooseDestination(Universe, Player)

    # Solution Suboptimal
    while interact_with_anomaly:

        # You have to fight ALL Enemies
        for enemy in anomaly.enemies:
            # Begin Fight
            emy.beginFight(Player.currentShip, enemy)
            # Remove Enemy
            anomaly.enemies.remove(enemy)

        # Must Find a better solution for this
        if anomaly.__class__.__name__ == 'Planet':
            # Arrive at Planet
            pi.Arrive(anomaly, Player)

        elif anomaly.__class__.__name__ == 'Spacegate':
            # Arrive at Spacegate
            sgi.Arrive(anomaly, Player)

        elif anomaly.__class__.__name__ == 'Starbase':
            # Arrive at Starbase
            sbi.Arrive(anomaly, Player)

        # Choose Next Destination
        interact_with_anomaly = ui.ChooseDestination(Universe, Player)
