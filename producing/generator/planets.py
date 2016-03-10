import random


def generatePlanetInformation(db):
    if not db.Planets.ListOfNames:
        return

    planetName = generatePlanetName(db)

    goodsConsumed = generateConsumedGoods(db)
    goodsProduced = generateProducedGoods(db, goodsConsumed)

    prices = generatePrices(db, goodsConsumed, goodsProduced)

    planetInformation = {
        'name': planetName,

        'goodsConsumed': goodsConsumed,
        'goodsProduced': goodsProduced,

        'prices': prices
    }

    return planetInformation


def generatePlanetName(db):
    possibleNames = db.Planets.ListOfNames

    planetName = random.choice(possibleNames)

    db.Planets.ListOfNames.remove(planetName)

    return planetName


def generateConsumedGoods(db):
    possibleGoods = db.Goods.ListOfNames

    numberofGoodsConsumed = random.randint(db.Goods.MinNumberOfGoodsConsumed, db.Goods.MaxNumberOfGoodsConsumed)

    goodsConsumed = list()

    while len(goodsConsumed) < numberofGoodsConsumed:
        good = random.choice(possibleGoods)

        if good not in goodsConsumed:
            goodsConsumed.append(good)

    return goodsConsumed


def generateProducedGoods(db, goodsConsumed):
    possibleGoods = db.Goods.ListOfNames

    numberOfGoodsProduced = random.randint(db.Goods.MinNumberOfGoodsProduced, db.Goods.MaxNumberOfGoodsProduced)

    goodsProduced = list()

    while len(goodsProduced) < numberOfGoodsProduced:
        good = random.choice(possibleGoods)

        if good not in goodsProduced:
            if good not in goodsConsumed:
                goodsProduced.append(good)

    return goodsProduced


def generatePrices(db, goodsConsumed, goodsProduced):
    prices = dict()
    for good in goodsConsumed:
        prices.update({good: random.randint(db.Goods.MinBuyPrice, db.Goods.MaxBuyPrice)})

    for good in goodsProduced:
        prices.update({good: random.randint(db.Goods.MinSellPrice, db.Goods.MaxSellPrice)})

    return prices
