
def chooseSection(Anomaly, Player, AvailableSections):
    # Flush Terminal
    print '\n' * 100

    # Border
    print '--' * 40

    # Information Screen
    information = generateInfoString(Anomaly, Player, AvailableSections=AvailableSections)
    print information

    # Option Screen
    # options = generateSectionsString(AvailableSections)
    # print options

    # Border
    print '--' * 40

    # Await Choice
    choice = raw_input()

    while True:

        if choice == '':
            return AvailableSections[-1]

        try:
            choice = int(choice)

            # Not Valid Choice
            if choice not in range(len(AvailableSections)):
                raise ValueError

            return AvailableSections[choice]

        except ValueError:
            print "Sorry %s not valid" % choice
            choice = raw_input()


def chooseInteraction(Anomaly, Player, Section, LastInteractionInfo):
    # Margin
    print '\n'*100
    # Border
    print '--' * 40

    # Gen Section Info
    secinfo = generateInfoString(Anomaly, Player, Section, LastInteractionInfo)
    print secinfo

    # Border
    print '--' * 40

    # Await Choice
    choice = raw_input()

    while True:
        if choice == '':
            if LastInteractionInfo != True:
                number = Section.index(LastInteractionInfo)

                return Section[number]

            return

        try:
            formatedChoice = int(choice)

            if formatedChoice not in range(len(Section)+1):
                raise ValueError

            if formatedChoice == 0:
                return

            return Section[formatedChoice-1]

        except ValueError:
            print "Sorry %s not valid" % choice
            choice = raw_input()


    # # Not Valid Choice
    # while choice not in range(len(Section)+1):
    #     print "Sorry %s not valid" % choice
    #     choice = input()

    # if choice == 0:
    #     return

    # return Section[choice-1]


def generateInfoString(Anomaly, Player, Section=True, LastInteractionInfo=None, AvailableSections=None):
    # Anomaly Type
    anomalyType = Anomaly.__class__.__name__
    # Init
    info = ''
    # Positonal Information
    info += "\n You are at %s %s" % (anomalyType, Anomaly.name)

    longInfo = """
        Current Stats:
            Credits: CREDS
            Attack:  ATTACK    Defense: DEFCURR/DEFMAX
            Maximum Travel Distance: TRAVELDIST
            Maintenance Costs: MAINTCOST

            Cargo Bay: CURRENTCARGO/MAXCARGO -> INCARGO

            Rooms:  CURRENTROOMS/MAXROOMS
                    ROOMS

        You are at ANOMALYTYPE ANOMALYNAME
    """

    # cargoBay = ''
    # for good, amount in Player.currentShip.inCargo.iteritems():
    #     cargoBay += "%s: %s " % (str(good), str(amount))

    longInfo = longInfo.replace('ANOMALYTYPE', anomalyType)

    longInfo = longInfo.replace('ANOMALYNAME', Anomaly.name)

    longInfo = longInfo.replace('CREDS', str(Player.credits))

    longInfo = longInfo.replace('CURRENTCARGO', str(Player.currentShip.cargoCapacity.startValue - Player.currentShip.cargoCapacity()))

    longInfo = longInfo.replace('MAXCARGO', str(Player.currentShip.cargoCapacity.startValue))

    longInfo = longInfo.replace('INCARGO', str(Player.currentShip.inCargo))

    longInfo = longInfo.replace('ATTACK', str(Player.currentShip.attackPower()))

    longInfo = longInfo.replace('DEFCURR', str(Player.currentShip.shieldStrength()))

    longInfo = longInfo.replace('DEFMAX', str(Player.currentShip.shieldStrength.startValue))

    longInfo = longInfo.replace('TRAVELDIST', str(Player.currentShip.maxTravelDistance()))

    longInfo = longInfo.replace('MAINTCOST', str(Player.currentShip.maintenanceCosts()))

    longInfo = longInfo.replace('CURRENTROOMS', str(Player.currentShip.spaceForRooms.startValue - Player.currentShip.spaceForRooms()))

    longInfo = longInfo.replace('MAXROOMS', str(Player.currentShip.spaceForRooms.startValue))

    roomString = ''
    for room in Player.currentShip.rooms:
        roomString += room.name + '  '
        for stat in room.statBoosts:
            roomString += stat.statName + ' ' + str(stat.startValue) + '  '
        roomString += '\n                    '

    longInfo = longInfo.replace('ROOMS', roomString)

    # Add Options
    if Section == True:
        longInfo += generateSectionsString(AvailableSections)
    else:
        longInfo += '\n\n\n'

    # Add Goods Produced
    try:
        infoExtension = """
        Merchant - Sells Goods:
            GOODSFORSALEINFO
        """

        goodsSaleInfo = ''
        for good in Anomaly.goodsProduced:
            goodsInfo = "< GOODNAME: GOODPRICE >  "

            goodsInfo = goodsInfo.replace('GOODNAME', good)

            goodsInfo = goodsInfo.replace('GOODPRICE', str(Anomaly.prices[good]))

            goodsSaleInfo += goodsInfo

        infoExtension = infoExtension.replace('GOODSFORSALEINFO', goodsSaleInfo)

        longInfo += infoExtension

        if Section.__class__.__name__ == 'Merchant':
            longInfo += generateInteractionsString(Section, LastInteractionInfo)
        else:
            longInfo += '\n\n'

    except AttributeError:
        pass

    # Add Goods Consumed
    try:
        infoExtension = """
        Trader - Buys Goods:
            GOODSBUYINFO
        """

        goodsBuyInfo = ''
        for good in Anomaly.goodsConsumed:
            goodsInfo = "< GOODNAME: GOODPRICE >  "

            goodsInfo = goodsInfo.replace('GOODNAME', good)

            goodsInfo = goodsInfo.replace('GOODPRICE', str(Anomaly.prices[good]))

            goodsBuyInfo += goodsInfo

        infoExtension = infoExtension.replace('GOODSBUYINFO', goodsBuyInfo)

        longInfo += infoExtension

        if Section.__class__.__name__ == 'Trader':
            longInfo += generateInteractionsString(Section, LastInteractionInfo)
        else:
            longInfo += '\n\n'

    except AttributeError:
        pass


    # Add Rooms For Sale
    try:
        roomSaleInfo = """      Equipment Dealer - Sells Rooms: \n"""
        for room in Anomaly.roomsForSale:
            roomInfo = """              ROOMNAME: Price: PRICE """

            roomInfo = roomInfo.replace('ROOMNAME', room.name)

            roomInfo = roomInfo.replace('PRICE', str(room.price))

            for statBoost in room.statBoosts:
                roomInfo += "/ STATNAME: STATVALUE "

                roomInfo = roomInfo.replace('STATNAME', statBoost.statName)

                roomInfo = roomInfo.replace('STATVALUE', str(statBoost.startValue))

            roomInfo += '\n'

            roomSaleInfo += roomInfo

        longInfo += roomSaleInfo

        if Section.__class__.__name__ == 'EquipmentDealer':
            longInfo += generateInteractionsString(Section, LastInteractionInfo)

    except AttributeError:
        pass

    return longInfo


# def generateSectionInfoString(Section, Player):
#     secInfo = 'Current Stats: \n'

#     for info in Section.correspondingStats:
#         value = Section.correspondingStats[info]
#         secInfo += " %s: %s \n" % (info, value)

#     return secInfo


def generateSectionsString(PossibleActions):
    # Init
    info = '\n          '
    # Option Information

    for interaction in PossibleActions:
        number = PossibleActions.index(interaction)

        if number == len(PossibleActions)-1:
            number = 'ENTER'

        info += '/ [%s] %s /' % (str(number), interaction.__class__.__name__)

    info += '\n \n'

    return info


def generateInteractionsString(Section, LastInteractionInfo):
    # Gen Action String
    actStr = """
            / [0] Back /"""

    if LastInteractionInfo == True:
        actStr = actStr.replace('0', 'ENTER')
    # Loop
    for interaction, info in Section:
        number = str(Section.index(interaction)+1)
        if LastInteractionInfo == interaction:
            number = 'ENTER'
        actStr += '/ [' + number + '] '

        actStr += Section.interactionType + ' ' + interaction

        # actStr += ' for ' + str(info) + ' /'
        actStr += ' /'

    actStr += '\n'

    return actStr
