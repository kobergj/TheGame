import multiprocessing
import random


# Models
import models.anomaly_models as mod
import models.ship_models as msp
import models.content_models as mro
import models.universe_models as muv
import models.player_models as mpl

# Generators
import controller.generator.ships as gsp
import controller.generator.rooms as gro

# Log
import configuration.log_details as log

def produceUniverse(MaxCoordinates=[15, 15], MinCoordinates=[0, 0]):
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
        good_to_loot = produceGood(Database)

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

    good = mro.Good(name)

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
    def __init__(self, database, connection):
        # Create Producer Thread
        self.producingThread = multiprocessing.Process(
            name='ModelProducer',
            target=self.__call__,
            # args=(database)
            )
        # Make Him a Daemon
        # self.producingThread.daemon = True

        # Set Kill Switch
        self.dead = False

        self.conn = connection

        self.db = database

    def __call__(self):
        log.log('Creating Player')
        player = producePlayer(self.db.StartConfiguration.PlayerInfo)

        log.log('Generating Universe')
        universe = produceUniverse(self.db.StartConfiguration.MaxCoordinates,
                                   self.db.StartConfiguration.MinCoordinates)

        log.log('Craft Ship')
        startingShip = produceShip(self.db, self.db.StartConfiguration.StartingShipStats)

        log.log('Board Ship')
        player.switchShip(startingShip)

        log.log('Set Starting Anomaly')
        startingAnomaly = produceAnomaly(self.db)
        universe.addAnomaly(startingAnomaly)
        player.travelTo(startingAnomaly.coordinates)

        log.log('Fill Universe')
        self.fill_universe(universe, self.db.StartConfiguration.NumberOfAnomalies)

        while True:
            log.log('Update Universe')
            self.update(universe, player)
            log.log('Sending Models')
            self.conn.send([universe, player])
            log.log('Awaiting Input')
            change_function = self.conn.recv()
            log.log('Executing Input')
            change_function(universe, player)

    def update(self, universe, player):
        if not universe.request_update:
            return

        for anomaly in universe:
            # Get Enemy from Queue
            newEnemy = produceEnemy(self.db)
            # Append to Enemy List
            if newEnemy:
                anomaly.enemies.append(newEnemy)

            try:
                # Get Ship
                ship = produceShip(self.db)

                # Attach Ship to Station
                anomaly.changeShipForSale(ship)
            except AttributeError:
                pass

            try:
                # Delete One Room
                if anomaly.roomsForSale:
                    anomaly.roomsForSale.pop(0)

                # Fill Room List
                while len(anomaly.roomsForSale) < anomaly.maxRoomsForSale:
                    # Get Room
                    room = produceRoom(self.db)

                    # Add Room
                    anomaly.addRoomForSale(room)
            except AttributeError:
                pass

        # Demock Stats
        player.currentShip.maxTravelDistance.demock()
        player.currentShip.maintenanceCosts.demock()


        universe.request_update = False


    def fill_universe(self, universe, NumberOfAnomalies):
        for i in range(NumberOfAnomalies):
            # Get Anomaly
            anomaly = produceAnomaly(self.db)
            # Add Anomaly
            universe.addAnomaly(anomaly)


    def startProducing(self):
        self.producingThread.start()

    def stopProducing(self):
        # Stop Process
        self.killProducer()
        self.producingThread.join()

    def killProducer(self):
        self.dead = True

    def producingFunction(self, Database, Universe):

        log.log('Start Model Producing')

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

        log.log('Model Producer dead and gone')
