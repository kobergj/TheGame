import random

POSSIBLE_NAMES = ['Earth', 'Mars', 'Venus', 'Jupiter', 'Vulcan', 'Kobol', "Quo'Nos", 'Galistrat C']

MAX_COORDINATES = [10, 10, 10]
MIN_COORDINATES = [-10, -10, -10]

MIN_NUMBER_GOODS_CONSUMED = 1
MAX_NUMBER_GOODS_CONSUMED = 3

MIN_NUMBER_GOODS_PRODUCED = 1
MAX_NUMBER_GOODS_PRODUCED = 3

POSSIBLE_GOODS = ['Gin', 'Videogames', 'Evil', 'BBQ Ribs', 'Airplanes', 'Mutton', 'Sand', 'Splice',
                  'Garlic', 'Ice Cubes', 'Slibbery Worms', 'Merchandise', 'Blunt Weapons']


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

    planetInformation = {
        'name': planetName,
        'coordinates': coordinates,

        'goodsConsumed': goodsConsumed,
        'goodsProduced': goodsProduced
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
