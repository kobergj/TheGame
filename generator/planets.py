import random
import database.database as db


POSSIBLE_NAMES = db.Planets.ListOfNames

MAX_COORDINATES = db.Universe.MaxCoordinates
MIN_COORDINATES = db.Universe.MinCoordinates

MIN_NUMBER_GOODS_CONSUMED = db.Goods.MinNumberOfGoodsConsumed
MAX_NUMBER_GOODS_CONSUMED = db.Goods.MaxNumberOfGoodsConsumed

MIN_NUMBER_GOODS_PRODUCED = db.Goods.MinNumberOfGoodsProduced
MAX_NUMBER_GOODS_PRODUCED = db.Goods.MaxNumberOfGoodsProduced

MIN_SELL_PRICE = db.Goods.MinSellPrice
MAX_SELL_PRICE = db.Goods.MaxSellPrice

MIN_BUY_PRICE = db.Goods.MinBuyPrice
MAX_BUY_PRICE = db.Goods.MaxBuyPrice

POSSIBLE_GOODS = db.Goods.ListOfNames


def generatePlanetList(numberOfPlanets):
    planetList = list()
    planetNamesList = list()

    while len(planetList) < numberOfPlanets:
        planet = generatePlanetInformation()

        if planet['name'] not in planetNamesList:
            planetList.append(planet)
            planetNamesList.append(planet['name'])

    return planetList


def generatePlanetInformation():
    planetName = generatePlanetName()
    coordinates = generateCoordinates()

    goodsConsumed = generateConsumedGoods()
    goodsProduced = generateProducedGoods(goodsConsumed)

    prices = generatePrices(goodsConsumed, goodsProduced)

    planetInformation = {
        'name': planetName,
        'coordinates': coordinates,

        'goodsConsumed': goodsConsumed,
        'goodsProduced': goodsProduced,

        'prices': prices
    }

    return planetInformation


def generatePlanetName():
    possibleNames = POSSIBLE_NAMES

    planetName = random.choice(possibleNames)

    return planetName


def generateCoordinates():
    maxCoordinates = MAX_COORDINATES
    minCoordinates = MIN_COORDINATES

    coordinates = list()

    for i in range(len(maxCoordinates)):
        coordinate = random.randint(minCoordinates[i], maxCoordinates[i])
        coordinates.append(coordinate)

    return coordinates


def generateConsumedGoods():
    possibleGoods = POSSIBLE_GOODS

    numberofGoodsConsumed = random.randint(MIN_NUMBER_GOODS_CONSUMED, MAX_NUMBER_GOODS_CONSUMED)

    goodsConsumed = list()

    while len(goodsConsumed) < numberofGoodsConsumed:
        good = random.choice(possibleGoods)

        if good not in goodsConsumed:
            goodsConsumed.append(good)

    return goodsConsumed


def generateProducedGoods(goodsConsumed):
    possibleGoods = POSSIBLE_GOODS

    numberOfGoodsProduced = random.randint(MIN_NUMBER_GOODS_PRODUCED, MAX_NUMBER_GOODS_PRODUCED)

    goodsProduced = list()

    while len(goodsProduced) < numberOfGoodsProduced:
        good = random.choice(possibleGoods)

        if good not in goodsProduced:
            if good not in goodsConsumed:
                goodsProduced.append(good)

    return goodsProduced


def generatePrices(goodsConsumed, goodsProduced):
    prices = dict()
    for good in goodsConsumed:
        prices.update({good: random.randint(MIN_BUY_PRICE, MAX_BUY_PRICE)})

    for good in goodsProduced:
        prices.update({good: random.randint(MIN_SELL_PRICE, MAX_SELL_PRICE)})

    return prices
