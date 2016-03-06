import random


def generateStarbaseInformation(db):
    starbaseName = generateStarbaseName(db)
    coordinates = generateCoordinates(db)

    maxRoomsforSale = generateMaxRoomsForSale(db)

    spacegateInformation = {
        'name': starbaseName,
        'coordinates': coordinates,
        'maxRoomsforSale': maxRoomsforSale,
    }

    return spacegateInformation


def generateStarbaseName(db):
    name = random.choice(db.Starbases.ListOfNames)

    return name


def generateCoordinates(db):
    maxCoordinates = db.Universe.MaxCoordinates
    minCoordinates = db.Universe.MinCoordinates

    coordinates = list()

    for i in range(len(maxCoordinates)):
        coordinate = random.randint(minCoordinates[i], maxCoordinates[i])
        coordinates.append(coordinate)

    return coordinates


def generateMaxRoomsForSale(db):
    maxNumber = 3

    return maxNumber
