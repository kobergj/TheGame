import random


def generateRoomInformation(db):
    # Name
    name = generateName()

    # Price
    price = generatePrice()

    # Assign Room Information:
    roomInformation = {'name': name,
                       'price': price
                       }

    return roomInformation


def generateName():
    name = 'room#'

    name += str(random.randint(0, 99))

    return name


def generatePrice():
    price = 0

    return price
