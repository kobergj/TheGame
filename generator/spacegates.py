import random


def generateSpacegateInformation(db):
    spacegateName = generateSpacegateName(db)

    costForUse = calculateCostForUse(db)

    spacegateInformation = {
        'name': spacegateName,

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


def calculateCostForUse(db):
    cost = db.Spacegates.CostForUse

    return cost
