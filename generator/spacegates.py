import random


def generateSpacegateInformation(db):
    spacegateName = generateSpacegateName(db)
    coordinates = generateCoordinates(db)

    costForUse = calculateCostForUse(db)

    spacegateInformation = {
        'name': spacegateName,
        'coordinates': coordinates,

        'costForUse': costForUse
    }

    return spacegateInformation


def generateSpacegateName(db):
    name = random.choice(db.Spacegates.Identifiers)

    currentId = random.randint(1, 100)

    if currentId <= 10:
        name = name.replace('XX', '0%s' % currentId)
    else:
        name = name.replace('XX', str(currentId))

    return name


def generateCoordinates(db):
    maxCoordinates = db.Universe.MaxCoordinates
    minCoordinates = db.Universe.MinCoordinates

    coordinates = list()

    for i in range(len(maxCoordinates)):
        coordinate = random.randint(minCoordinates[i], maxCoordinates[i])
        coordinates.append(coordinate)

    return coordinates


def calculateCostForUse(db):
    cost = db.Spacegates.CostForUse

    return cost
