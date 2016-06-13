import random
import multiprocessing as mp

import models.universe_models as um
import models.player_models as pm
import models.anomaly_models as am
import models.content_models as cm


# Generic Class

class ModelProducer:
    def __init__(self, model):

        self.model_class = model

    def __call__(self, *args):
        model = self.model_class(*args)

        return model

    def random(self, listofnames):
        name = random.choice(listofnames)

        return self(name)

# General Classes

class UniverseProducer(ModelProducer):
    def random(self):
        minco = self.db.MinCoordinates
        maxco = self.db.MaxCoordinates

        return self(minco, maxco)

class PlayerProducer(ModelProducer):
    def random(self):
        pl_info = self.db.PlayerInfo

        return self(pl_info)

# Anomalies

class PlanetProducer(ModelProducer):
    def random(self):
        if not self.db.ListOfNames:
            # Returns None if no Names left
            return

        name = random.choice(self.db.ListOfNames)

        self.db.ListOfNames.remove(name)

        return self(name)

class SpacegateProducer(ModelProducer):
    def random(self):
        name = self.db.IdentifiersList[0]

        while name in self.db.IdentifiersList:

            currentId = random.randint(1, 1000)

            name += str(currentId)

        self.db.IdentifiersList.append(name)

        return self(name)

class StarbaseProducer(ModelProducer):
    def random(self):
        if not self.db.ListOfNames:
            return

        name = random.choice(self.db.ListOfNames)

        self.db.ListOfNames.remove(name)

        return self(name)

class GoodProducer(ModelProducer):
    def random(self):
        name = random.choice(self.db.ListOfNames)

        return self(name)

class ModelProducerProcess(mp.Process):
    def __init__(self, database, connection):
        mp.Process.__init__(self, name='ModelProducer')

        self.connection = connection

        self._universeproducer = UniverseProducer(database.Universe)

        self._playerproducer = PlayerProducer(database.StartConfiguration)

        self._planetproducer = PlanetProducer(database.Planets)
        self._starbaseproducer = StarbaseProducer(database.Starbases)
        self._spacegateproducer = SpacegateProducer(database.Spacegates)

        self._goodproducer = GoodProducer(database.Goods)

    def run(self):
        player = self._playerproducer.random()

        universe = self._universeproducer.random()








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
