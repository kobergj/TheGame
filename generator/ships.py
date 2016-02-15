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
                 'spaceForRooms': spaceForRooms
                 }

    return shipStats


def generateStat(bounds):
    stat = random.randint(bounds[0], bounds[1])

    return stat
