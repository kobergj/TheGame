import random


def generateRoomInformation(Database):
    # Level
    roomLevel = generateRoomLevel()

    # Stats
    stats = generateStats(Database, roomLevel)

    # Name
    name = generateName(Database, stats)

    # Price
    price = generatePrice(stats)

    # Assign Room Information:
    roomInformation = {'name':          name,
                       'level':         roomLevel,

                       'statBoosts':    stats,
                       'price':         price,
                       }

    return roomInformation


def generateName(Database, Stats):
    name = ''
    for statInfo in Stats:
        stat = statInfo[0]
        name += random.choice(Database.Rooms.RoomNameParts[stat])
        name += ' '

    name += random.choice(Database.Rooms.RoomNameParts['roomType'])

    return name


def generateStats(Database, RoomLevel):
    statBoosts = list()

    for i in range(RoomLevel):
        stat = random.choice(Database.Rooms.StatBoosts.keys())

        boostBounds = Database.Rooms.StatBoosts[stat]

        boost = random.randint(*boostBounds)

        statBoosts.append([stat, boost])

    return statBoosts


def generatePrice(stats):
    price = 0

    for stat, value in stats:
        price += (value*20)

    return price


def generateRoomLevel():

    i = random.randint(0, 100)

    if i > 90:
        level = 3
    elif i > 60:
        level = 2
    else:
        level = 1

    return level
