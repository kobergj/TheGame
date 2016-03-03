import controller.planet_interactions as pi
import controller.spacegate_interactions as sgi
import controller.starbase_interactions as sbi
import controller.enemy_interactions as emy


def Arrive(Player, Anomaly):
        # Check for Enemies
        if Anomaly.enemies:
            # You have to fight ALL Enemies
            for enemy in Anomaly.enemies:
                # Begin Fight
                emy.beginFight(Player.currentShip, enemy)

        # Must Find a better solution for this
        if Anomaly.__class__.__name__ == 'Planet':
            # Arrive at Planet
            pi.Arrive(Anomaly, Player)

        elif Anomaly.__class__.__name__ == 'Spacegate':
            # Arrive at Spacegate
            sgi.Arrive(Anomaly, Player)

        elif Anomaly.__class__.__name__ == 'Starbase':
            # Arrive at Starbase
            sbi.Arrive(Anomaly, Player)
