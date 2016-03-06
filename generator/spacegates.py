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
    name = db.Spacegates.IdentifiersList[0]

    while name in db.Spacegates.IdentifiersList:

        currentId = random.randint(1, 1000)

        name += str(currentId)

    db.Spacegates.IdentifiersList.append(name)

    return name


def generateCoordinates(db):
    maxCoordinates = db.Universe.MaxCoordinates
    minCoordinates = db.Universe.MinCoordinates

    coordinates = db.Universe.RestrictedCoordinates[0]

    while coordinates in db.Universe.RestrictedCoordinates:
        coordinates = list()

        for i in range(len(maxCoordinates)):
            coordinate = random.randint(minCoordinates[i], maxCoordinates[i] + 1)
            coordinates.append(coordinate)

    db.Universe.RestrictedCoordinates.append(coordinates)

    return coordinates


def calculateCostForUse(db):
    cost = db.Spacegates.CostForUse

    return cost
