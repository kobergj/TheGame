
def generateRoomInformation():
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
    name = 'roomName'

    return name


def generatePrice():
    price = 0

    return price
