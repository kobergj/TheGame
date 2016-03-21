# Models
import producing.models.anomalies as mod
import producing.models.ships as msp
import producing.models.ship_content as mro
import producing.models.universe as muv
import producing.models.player as mpl

# Generators
import producing.generator.planets as gpl
import producing.generator.spacegates as gsg
import producing.generator.starbases as gsb
import producing.generator.ships as gsp
import producing.generator.rooms as gro

import threading
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


def produceUniverse(MaxCoordinates, MinCoordinates=[0, 0]):
    """Produces a Universe with the given Coordinates """
    universe = muv.Universe(MinCoordinates, MaxCoordinates)

    return universe


def producePlayer(PlayerInfo):
    """Produces a Player."""
    player = mpl.Player(PlayerInfo)

    return player


def produceAnomaly(Database, anomalyInfo=None):
    """Produces a Anomaly. Creates Random Stats if not given"""
    while not anomalyInfo:
        # Choose Anomaly Type
        anomalyType = random.choice(Database.Universe.AnomalyTypes)

        # Get Info Func
        genInfo = ANOMALY_INFO_FUNCS[anomalyType]

        # Get Info
        anomalyInfo = genInfo(Database)

    # Get Model
    model = ANOMALY_MODELS[anomalyType]

    # Create Anomaly
    anomaly = model(anomalyInfo)

    return anomaly


def produceShip(Database, shipInfo=None):
    """Produces a Ship. Creates Random Stats if not given"""
    if not shipInfo:
        # Generate Ship Info
        shipInfo = gsp.generateShipInformation(Database)

    # Create Ship
    ship = msp.Ship(shipInfo)

    return ship


def produceRoom(Database, roomInfo=None):
    """Produces a Room. Creates Random Stats if not given"""
    if not roomInfo:
        # Generate Room Info
        roomInfo = gro.generateRoomInformation(Database)

    # Create Room
    room = mro.Room(roomInfo)

    return room


def produceEnemy(Database, enemyInfo=None):
    """Produces an Enemy. Creates Random Stats if not given"""
    if not enemyInfo:
        # generate Enemy Information - For the moment only Ships
        enemyInfo = gsp.generateShipInformation(Database)
        # generate Enemy
        enemy = msp.Enemy(enemyInfo)

    # Add Loot Credits
    creds_to_loot = enemy.attackPower() + enemy.shieldStrength()
    enemy.addMoreCredits(creds_to_loot)

    # Loot Goods
    for i in range(random.randint(1, 5)):
        good_to_loot = random.choice(Database.Goods.ListOfNames)

        enemy.loadCargo(good_to_loot)

    # Random Number
    i = random.randint(0, 100)

    # Enemy Probability
    if i > Database.Universe.EnemyProbability:
        # Lucky you are...
        enemy = None

    return enemy


class randomProducer():
    """Gets a Database to work on and a Universe to play with.
        Randomly Produces:
            Planets
            Starbases
            Spacegates

            Rooms
            Ships

            Enemies"""

    # For the Moment Only One Universe per Producer
    def __init__(self, Database, Universe):
        # Create Producer Thread
        self.producingThread = threading.Thread(
            name='ProducingThread',
            target=self.producingFunction,
            args=(Database, Universe)
            )
        # Make Him a Daemon
        self.producingThread.daemon = True

        # Set Kill Switch
        self.dead = False

    def startProducing(self):
        self.producingThread.start()

    def killProducer(self):
        self.dead = True

    def producingFunction(self, Database, Universe):

        while not self.dead:
            # Anomalies
            while not Universe.anomalyQ.full():
                # Produce Anomaly
                anomaly = produceAnomaly(Database)

                # Put In Q
                Universe.anomalyQ.put(anomaly)

            # Ships
            while not Universe.shipQ.full():
                # Produce Ship
                ship = produceShip(Database)

                # Put In Q
                Universe.shipQ.put(ship)

            # Rooms
            while not Universe.roomQ.full():
                # Produce Room
                room = produceRoom(Database)

                # Put in Q
                Universe.roomQ.put(room)

            # Enemies
            while not Universe.enemyQ.full():
                # Produce Enemy
                enemy = produceEnemy(Database)

                # Put in Q
                Universe.enemyQ.put(enemy)
