import random
import database.database as db


def generateShipInformation():
    cargoCapacity = generateStat(db.Ships.Cargobounds)
    speed = generateStat(db.Ships.Speedbounds)
    maxTravelDistance = generateStat(db.Ships.Travelbounds)
    spaceForRooms = generateStat(db.Ships.Roombounds)

    shipStats = {'cargoCapacity': cargoCapacity,
                 'speed': speed,
                 'maxTravelDistance': maxTravelDistance,
                 'spaceForRooms': spaceForRooms,

                 }

    # Calc Price
    shipPrice = calculateShipPrice(shipStats)

    # Update Stats
    shipStats.update({'price': shipPrice})

    return shipStats


def generateStat(bounds):
    stat = random.randint(bounds[0], bounds[1])

    return stat


def calculateShipPrice(shipStats):
    price = 0
    for value in shipStats.values():
        price += value * 10

    price += random.randint(1-price, 200)

    return price
