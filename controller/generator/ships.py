import random


def generateShipInformation(Database):
    shipDB = Database.Ships.__dict__

    shipClass = random.choice(shipDB['ShipClasses'])

    boundDict = Database.Ships.__dict__[shipClass].bounds

    shipStats = dict()

    for stat, modifier in boundDict.iteritems():
        minValue = shipDB[stat] + modifier[0]
        maxValue = shipDB[stat] + modifier[1]

        statValue = random.randint(minValue, maxValue)

        shipStats.update({stat: statValue})

    # Calc Price
    shipPrice = calculateShipPrice(shipStats)

    # Update Stats
    shipStats.update({'price': shipPrice})

    return shipStats


# def generateStat(bounds):
#     stat = random.randint(bounds[0], bounds[1])

#     return stat


def calculateShipPrice(shipStats):
    price = 0
    for value in shipStats.values():
        price += value * 10

    # price += random.randint(1-price, 200)

    return price
