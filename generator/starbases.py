import random
import database.database as db


def generateStarbaseList(numberOfStarbases):
    starbaseList = list()

    while len(starbaseList) < numberOfStarbases:
        starbase = generateStarbaseInformation()
        starbaseList.append(starbase)

    return starbaseList


def generateStarbaseInformation():
    starbaseName = generateStarbaseName()
    coordinates = generateCoordinates()

    maxRoomsforSale = generateMaxRoomsForSale()

    spacegateInformation = {
        'name': starbaseName,
        'coordinates': coordinates,
        'maxRoomsforSale': maxRoomsforSale,
    }

    return spacegateInformation


def generateStarbaseName():
    name = random.choice(db.Starbases.ListOfNames)

    return name


def generateCoordinates():
    maxCoordinates = db.Universe.MaxCoordinates
    minCoordinates = db.Universe.MinCoordinates

    coordinates = list()

    for i in range(len(maxCoordinates)):
        coordinate = random.randint(minCoordinates[i], maxCoordinates[i])
        coordinates.append(coordinate)

    return coordinates


def generateMaxRoomsForSale():
    maxNumber = 3

    return maxNumber
