import models.anomalies as mod
import models.ships as msp
import models.rooms as mro

import generator.planets as gpl
import generator.spacegates as gsg
import generator.starbases as gsb

import generator.ships as gsp
import generator.rooms as gro

import random


ANOMALY_INFO_FUNCS = {
    'Planet':       gpl.generatePlanetInformation,
    'Starbase':     gsb.generateStarbaseInformation,
    'Spacegate':    gsg.generateSpacegateInformation,
}

ANOMALY_MODELS = {
    'Planet': mod.Planet,
    'Starbase': mod.Starbase,
    'Spacegate': mod.Spacegate,
}


def Producer(Database, Universe):
    """Produces:
            Planets
            Starbases
            Spacegates

            Rooms
            Ships

            Enemies"""

    # For the Moment Only One Universe per Producer

    while True:
        # Anomalies
        while not Universe.anomalyQ.full():
            # Choose Anomaly Type
            anomalyType = random.choice(Database.Universe.AnomalyTypes)

            # Get Info Func
            genInfo = ANOMALY_INFO_FUNCS[anomalyType]
            # Get Info
            anomalyInfo = genInfo(Database)

            if anomalyInfo:
                # Get Model
                model = ANOMALY_MODELS[anomalyType]
                # Create Anomaly
                anomaly = model(anomalyInfo)

                # Put In Q
                Universe.anomalyQ.put(anomaly)

            # # I dont like if clauses...
            # # Add Planet
            # if all([anomalyType == 'Planet', Database.Planets.ListOfNames]):
            #     planetinfo = gpl.generatePlanetInformation(Database)

            #     planet = mod.Planet(planetinfo)

            #     Universe.anomalyQ.put(planet)

            # # Add Starbase
            # elif all([anomalyType == 'Starbase', Database.Starbases.ListOfNames]):
            #     starbaseinfo = gsb.generateStarbaseInformation(Database)

            #     starbase = mod.Starbase(starbaseinfo)

            #     Universe.anomalyQ.put(starbase)

            # # Add Spacegate
            # elif anomalyType == 'Spacegate':
            #     spacegateinfo = gsg.generateSpacegateInformation(Database)

            #     spacegate = mod.Spacegate(spacegateinfo)

            #     Universe.anomalyQ.put(spacegate)

        # Ships
        while not Universe.shipQ.full():
            shipinfo = gsp.generateShipInformation(Database)

            ship = msp.Ship(shipinfo)

            Universe.shipQ.put(ship)

        # Rooms
        while not Universe.roomQ.full():
            roominfo = gro.generateRoomInformation(Database)

            room = mro.Room(roominfo)

            Universe.roomQ.put(room)

        # Enemies
        while not Universe.enemyQ.full():
            # generate Stats for Enemy Ship
            enemyShipInformation = gsp.generateShipInformation(Database)
            # generate Enemys
            enemyShip = msp.Ship(enemyShipInformation)

            # Random Number
            i = random.randint(0, 100)

            # Enemy Probability
            if i > Database.Universe.EnemyProbability:
                enemyShip = None

            Universe.enemyQ.put(enemyShip)
