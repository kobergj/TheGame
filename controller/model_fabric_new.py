import random
import multiprocessing as mp
import logging

import models.universe_models as um
import models.player_models as pm
import models.anomaly_models as am
import models.content_models as cm
import models.ship_models as sm


# Generic Class

log = logging.getLogger('model')

class ModelProducer:
    def __init__(self, database):

        self._database = database

        self._usednames = list()

    def starting_universe(self):
        db = self._database.StartConfiguration.Universe

        universe = um.Universe(db.MinCoordinates, db.MaxCoordinates)

        log.info('Filling Universe')
        while len(universe) < db.NumberOfAnomalies:
            kwargsdict = {'Planet': dict(merchant=True),
                          'Spacegate': dict(jumpgate=True)
                          }

            anmytype = random.choice(kwargsdict.keys())

            anomaly = self.random_anomaly(anmytype, **kwargsdict[anmytype])
            universe.addAnomaly(anomaly)

        return universe

    def starting_player(self):
        db = self._database.StartConfiguration.Player

        name = db.PlayerName
        crds = db.PlayerCredits

        ship = self.starting_ship()

        model = pm.Player(name, crds, ship)

        return model

    def starting_ship(self):
        shipdb = self._database.StartConfiguration.Ship

        name = shipdb.Name

        cargobay = cm.CargoBay(*shipdb.CargoBay)

        energycore = cm.EnergyCore(*shipdb.EnergyCore)

        engine = cm.Engine(*shipdb.Engine)

        weapon = cm.Weapon(*shipdb.Weapon)

        shield = cm.Shield(*shipdb.Shield)

        ship = sm.Ship(name, [cargobay, energycore, engine, weapon, shield])

        return ship

    def random_anomaly(self, anmtype, merchant=False, jumpgate=False):
        db = self._database.Anomalies

        log.info('Generating Planet Name')
        possiblenames = [name for name in db.ListOfNames if name not in self._usednames]
        planetname = random.choice(possiblenames)
        self._usednames.append(planetname)

        goods = None
        if merchant:
            log.info('Generating Goods')
            i = random.randint(*db.NumberOfGoods)
            goods = self.random_goodlist(i)

        jg_costs = None
        if jumpgate:
            log.info('Calculating SG Costs')
            jg_costs = random.randint(*db.SpaceGateCosts)

        log.info('Generating Enemies')
        enemies = list()

        model = am.Anomaly(planetname, anmtype, enemies, goods, jg_costs)

        return model

    def random_goodlist(self, length):
        db = self._database.Goods
        goods = list()

        while length > 0:
            name = random.choice(db.ListOfNames)

            if name in goods:
                continue

            price = random.randint(db.MinPrice, db.MaxPrice)

            good = cm.Good(name, price)

            goods.append(good)

            length -= 1

        return goods


    # def random_ship(self):
    #     db = self._database.Ships

    #     name = random.choice(db.ListOfNames)

    #     starting_content = [cm.CargoBay(), cm.EnergyCore(), cm.Engine(), cm.Weapon(), cm.Shield()]

    #     ship = sm.Ship(name, starting_content)

    #     return ship

# class SpacegateProducer(ModelProducer):
#     def random(self):
#         name = self.db.IdentifiersList[0]

#         while name in self.db.IdentifiersList:

#             currentId = random.randint(1, 1000)

#             name += str(currentId)

#         self.db.IdentifiersList.append(name)

#         return self(name)

# class StarbaseProducer(ModelProducer):
#     def random(self):
#         if not self.db.ListOfNames:
#             return

#         name = random.choice(self.db.ListOfNames)

#         self.db.ListOfNames.remove(name)

#         return self(name)

# class GoodProducer(ModelProducer):
#     def random(self):
#         name = random.choice(self.db.ListOfNames)

#         return self(name)

class ModelHandler(mp.Process):
    def __init__(self, database, connection):
        mp.Process.__init__(self, name='ModelProducer')

        self._connection = connection

        self._modelproducer = ModelProducer(database)

    def run(self):
        log.info('Creating Player')
        player = self._modelproducer.starting_player()
        log.info('Generating Universe')
        universe = self._modelproducer.starting_universe()
        log.info('Travel To Starting Anomaly')
        player.travelTo(random.choice([anomaly.coordinates for anomaly in universe]))

        log.info('Entering Main Loop')
        while True:

            if universe.request_update:
                self._updateuniverse(universe, player)

            log.info('Sending %s' % [universe, player])
            self._connection.send([universe, player])
            log.info('Awaiting Input')
            change_function = self._connection.recv()

            if change_function is None:
                log.info('Got Dead Signal. Quitting...')
                break

            log.info('Executing Input')
            change_function(universe, player)

        log.info('Model Producer Dead and gone')


    def _updateuniverse(self, universe, player):
        # for anomaly in universe:
        #     # Demock Stats
        #     player.currentShip.maxTravelDistance.demock()
        #     player.currentShip.maintenanceCosts.demock()


            universe.request_update = False



    # def _generateuniverse(self):
    #     db = self._database.Universe

    #     universe = self._modelproducer.static_universe()


    #     return universe








class Depr:
    def depr(self):
        # Add Consume
        if not produced_goods:
            min_goods = db.MinNumberOfGoodsConsumed
            max_goods = db.MaxNumberOfGoodsConsumed
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
