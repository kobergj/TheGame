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

    db.Starbases.ListOfNames.remove(name)

    return name


def generateCoordinates(db):
    maxCoordinates = db.Universe.MaxCoordinates
    minCoordinates = db.Universe.MinCoordinates

    coordinates = db.Universe.RestrictedCoordinates[0]

    while coordinates in db.Universe.RestrictedCoordinates:
        coordinates = list()

        for i in range(len(maxCoordinates)):
            coordinate = random.randint(minCoordinates[i], maxCoordinates[i])
            coordinates.append(coordinate)

    db.Universe.RestrictedCoordinates.append(coordinates)

    return coordinates


def generateMaxRoomsForSale(db):
    maxNumber = 3

    return maxNumber
