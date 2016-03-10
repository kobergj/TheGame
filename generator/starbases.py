import random


def generateStarbaseInformation(db):
    if not db.Starbases.ListOfNames:
        return

    starbaseName = generateStarbaseName(db)

    maxRoomsforSale = generateMaxRoomsForSale(db)

    spacegateInformation = {
        'name': starbaseName,

        'maxRoomsforSale': maxRoomsforSale,
    }

    return spacegateInformation


def generateStarbaseName(db):
    name = random.choice(db.Starbases.ListOfNames)

    db.Starbases.ListOfNames.remove(name)

    return name


def generateMaxRoomsForSale(db):
    maxNumber = 3

    return maxNumber
