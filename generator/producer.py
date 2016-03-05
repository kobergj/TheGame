import models as mod
import generator as gen
import database.database as db

import random


def Producer(Universe):
    """Produces various Items.

       For the Moment only Enemies included.

       Could be extended for rooms, ships, anomalies etc."""

    while True:
        # Loop through Anomalies
        for anomaly in Universe.anomalyList.values():
            # Enemies
            while not anomaly.enemyQ.full():
                # generate Stats for Enemy Ship
                enemyShipInformation = gen.ships.generateShipInformation()
                # generate Enemys
                enemyShip = mod.ships.Ship(enemyShipInformation)

                # Random Number
                i = random.randint(0, 100)

                # Enemy Probability
                if i <= db.Universe.EnemyProbability:
                    enemyShip = None

                anomaly.enemyQ.put(enemyShip)
