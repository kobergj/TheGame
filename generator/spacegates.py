import random
import database.database as db


def generateSpacegateList(numberOfSpacegates):
    spacegateList = list()

    while len(spacegateList) < numberOfSpacegates:
        spacegate = generateSpacegateInformation()
        spacegateList.append(spacegate)

    return spacegateList


def generateSpacegateInformation():
    spacegateName = generateSpacegateName()
    coordinates = generateCoordinates()

    costForUse = calculateCostForUse()

    spacegateInformation = {
        'name': spacegateName,
        'coordinates': coordinates,

        'costForUse': costForUse
    }

    return spacegateInformation


def generateSpacegateName():
    name = random.choice(db.Spacegates.Identifiers)

    currentId = random.randint(1, 100)

    if currentId <= 10:
        name = name.replace('XX', '0%s' % currentId)
    else:
        name = name.replace('XX', str(currentId))

    return name


def generateCoordinates():
    maxCoordinates = db.Universe.MaxCoordinates
    minCoordinates = db.Universe.MinCoordinates

    coordinates = list()

    for i in range(len(maxCoordinates)):
        coordinate = random.randint(minCoordinates[i], maxCoordinates[i])
        coordinates.append(coordinate)

    return coordinates


def calculateCostForUse():
    cost = db.Spacegates.CostForUse

    return cost
