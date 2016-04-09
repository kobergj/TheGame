# Models
import producing.models.anomalies as mod
import producing.models.ships as msp
import producing.models.ship_content as mro
import producing.models.universe as muv
import producing.models.player as mpl

# Generators
import producing.generator.ships as gsp
import producing.generator.rooms as gro

import threading
import random


def produceUniverse(MaxCoordinates, MinCoordinates=[0, 0]):
    """Produces a Universe with the given Coordinates """
    universe = muv.Universe(MinCoordinates, MaxCoordinates)

    return universe


def producePlayer(PlayerInfo):
    """Produces a Player."""
    player = mpl.Player(PlayerInfo)

    return player


def produceAnomaly(Database):
    """Produces a random anomaly. """
    anomaly_producers = [producePlanet,
                         produceStarbase,
                         produceSpacegate,
                        ]

    anomaly = None

    while not anomaly:
        # Choose Anomaly Type
        anomalyProducer = random.choice(anomaly_producers)

        # Get Info
        anomaly = anomalyProducer(Database)

    return anomaly


def producePlanet(Database, name=None):
    """Produces Planet. Takes Random Name if not given
        Fills it with random Goods. 
        Returns None if no names left"""
    if not name:

        if not Database.Planets.ListOfNames:
            return

        name = random.choice(Database.Planets.ListOfNames)

        Database.Planets.ListOfNames.remove(name)

    planet = mod.Planet(name)

    # Add Consume
    min_goods = Database.Planets.MinNumberOfGoodsConsumed
    max_goods = Database.Planets.MaxNumberOfGoodsConsumed
    num = random.randint(min_goods, max_goods)

    poss_goods = Database.Goods.ListOfNames[:]

    while len(planet.goodsConsumed) < num:
        good_name = random.choice(poss_goods)

        poss_goods.remove(good_name)

        min_price = Database.Goods.MinBuyPrice
        max_price = Database.Goods.MaxBuyPrice
        
        price = random.randint(min_price, max_price)

        good = mro.Good(good_name, price)

        planet.raiseConsume(good)

    # Add Produce
    min_goods = Database.Planets.MinNumberOfGoodsProduced
    max_goods = Database.Planets.MaxNumberOfGoodsProduced
    num = random.randint(min_goods, max_goods)

    while len(planet.goodsProduced) < num:
        good_name = random.choice(poss_goods)

        poss_goods.remove(good_name)

        min_price = Database.Goods.MinSellPrice
        max_price = Database.Goods.MaxSellPrice
        
        price = random.randint(min_price, max_price)

        good = mro.Good(good_name, price)

        planet.raiseProducing(good)

    return planet

def produceSpacegate(Database, name=None):
    if not name:
        name = Database.Spacegates.IdentifiersList[0]

        while name in Database.Spacegates.IdentifiersList:

            currentId = random.randint(1, 1000)

            name += str(currentId)

        Database.Spacegates.IdentifiersList.append(name)

    spacegate = mod.Spacegate(name)

    return spacegate

def produceStarbase(Database, name=None):
    if not name:

        if not Database.Starbases.ListOfNames:
            return

        name = random.choice(Database.Starbases.ListOfNames)

        Database.Starbases.ListOfNames.remove(name)

    starbase = mod.Starbase(name)

    return starbase



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
        good_to_loot = produceGood

        enemy.loadCargo(good_to_loot)

    # Random Number
    i = random.randint(0, 100)

    # Enemy Probability
    if i > Database.Universe.EnemyProbability:
        # Lucky you are...
        enemy = None

    return enemy

def produceGood(Database, name=None):
    """Produces a Good. Creates Random Name if not given"""
    if not name:
        name = random.choice(Database.Goods.ListOfNames)

    good = mro.Goods(name)

    return good


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
