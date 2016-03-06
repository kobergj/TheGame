import models.anomalies as mod
import models.ships as msp
import models.rooms as mro

import generator.planets as gpl
import generator.spacegates as gsg
import generator.starbases as gsb
import generator.ships as gsp
import generator.rooms as gro

import random


def Producer(Database, Universe):
    """Produces various Items.

       For the Moment only Enemies included.

       Could be extended for rooms, ships, anomalies etc."""

    # For the Moment Only One Universe per Producer

    while True:
        while not Universe.anomalyQ.full():
            # Choose Anomaly Type
            anomalyType = random.choice(Database.Universe.AnomalyTypes)

            # I dont like if clauses...
            # Add Planet
            if anomalyType == 'Planet':
                planetinfo = gpl.generatePlanetInformation(Database)

                planet = mod.Planet(planetinfo)

                Universe.anomalyQ.put(planet)

            # Add Starbase
            elif anomalyType == 'Starbase':
                starbaseinfo = gsb.generateStarbaseInformation(Database)

                starbase = mod.Starbase(starbaseinfo)

                Universe.anomalyQ.put(starbase)

            # Add Spacegate
            elif anomalyType == 'Spacegate':
                spacegateinfo = gsg.generateSpacegateInformation(Database)

                spacegate = mod.Spacegate(spacegateinfo)

                Universe.anomalyQ.put(spacegate)

        # Loop through Anomalies
        for anomaly in Universe.anomalyList.values():
            # Enemies
            while not anomaly.enemyQ.full():
                # generate Stats for Enemy Ship
                enemyShipInformation = gsp.generateShipInformation(Database)
                # generate Enemys
                enemyShip = msp.Ship(enemyShipInformation)

                # Random Number
                i = random.randint(0, 100)

                # Enemy Probability
                if i <= Database.Universe.EnemyProbability:
                    enemyShip = None

                anomaly.enemyQ.put(enemyShip)

            # Ships
            if hasattr(anomaly, 'shipQ'):
                while not anomaly.shipQ.full():
                    shipinfo = gsp.generateShipInformation(Database)

                    ship = msp.Ship(shipinfo)

                    anomaly.shipQ.put(ship)

            # Rooms
            if hasattr(anomaly, 'roomQ'):
                while not anomaly.roomQ.full():
                    roominfo = gro.generateRoomInformation(Database)

                    room = mro.Room(roominfo)

                    anomaly.roomQ.put(room)
