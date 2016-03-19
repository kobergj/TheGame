
def chooseSection(Anomaly, Player, AvailableSections):
    # Flush Terminal
    print '\n' * 100

    # Border
    print '--' * 20

    # Information Screen
    information = generateInfoString(Anomaly, Player)
    print information

    # Border
    print '--' * 20

    # Option Screen
    options = generateSectionsString(AvailableSections)
    print options

    # Await Choice
    choice = input()

    # Not Valid Choice
    while choice not in range(len(AvailableSections)):
        print "Sorry %s not valid" % choice
        choice = input()

    return AvailableSections[choice]


def chooseInteraction(Anomaly, Player, Section, LastInteractionInfo):
    # Margin
    print '\n'*100
    # Border
    print '--' * 20
    # Gen Section Info
    secinfo = generateInfoString(Anomaly, Player)
    print secinfo
    # Last Interaction
    if LastInteractionInfo is not True:
        print "%s: %s" % (Section.interactionType, LastInteractionInfo)
    # Gen Str
    interactions = generateInteractionsString(Section, LastInteractionInfo)
    print interactions
    # Await Choice
    choice = input()

    # Not Valid Choice
    while choice not in range(len(Section)+1):
        print "Sorry %s not valid" % choice
        choice = input()

    if choice == 0:
        return

    return Section[choice-1]


def generateInfoString(Anomaly, Player):
    # Anomaly Type
    anomalyType = Anomaly.__class__.__name__
    # Init
    info = ''
    # Positonal Information
    info += "\n You are at %s %s" % (anomalyType, Anomaly.name)

    longInfo = """
    You are at ANOMALYTYPE ANOMALYNAME
    Current Stats:
     Credits: CREDS

     Attack:  ATTACK        Defense: DEFENSE

     Maximum Travel Distance: TRAVELDIST 
     Maintenance Costs: MAINTCOST

     Cargo Bay: CURRENTCARGO/MAXCARGO
            INCARGO

     Rooms: CURRENTROOMS/MAXROOMS
            ROOMS
    """

    # cargoBay = ''
    # for good, amount in Player.currentShip.inCargo.iteritems():
    #     cargoBay += "%s: %s " % (str(good), str(amount))

    longInfo = longInfo.replace('ANOMALYTYPE', anomalyType)

    longInfo = longInfo.replace('ANOMALYNAME', Anomaly.name)

    longInfo = longInfo.replace('CREDS', str(Player.credits))

    longInfo = longInfo.replace('CURRENTCARGO', str(Player.currentShip.cargoCapacity()))

    longInfo = longInfo.replace('MAXCARGO', str(Player.currentShip.cargoCapacity.startValue))

    longInfo = longInfo.replace('INCARGO', str(Player.currentShip.inCargo))

    longInfo = longInfo.replace('ATTACK', str(Player.currentShip.attackPower()))

    longInfo = longInfo.replace('DEFENSE', str(Player.currentShip.shieldStrength()))

    longInfo = longInfo.replace('TRAVELDIST', str(Player.currentShip.maxTravelDistance()))

    longInfo = longInfo.replace('MAINTCOST', str(Player.currentShip.maintenanceCosts()))

    longInfo = longInfo.replace('CURRENTROOMS', str(Player.currentShip.spaceForRooms()))

    longInfo = longInfo.replace('MAXROOMS', str(Player.currentShip.spaceForRooms.startValue))

    roomString = ''
    for room in Player.currentShip.rooms:
        roomString += room.name + '  '
        for stat in room.statBoosts:
            roomString += stat.statName + ' ' + str(stat.startValue) + '  '
        roomString += '\n'

    longInfo = longInfo.replace('ROOMS', roomString)

    return longInfo


def generateSectionInfoString(Section, Player):
    secInfo = 'Current Stats: \n'

    for info in Section.correspondingStats:
        value = Section.correspondingStats[info]
        secInfo += " %s: %s \n" % (info, value)

    return secInfo


def generateSectionsString(PossibleActions):
    # Init
    info = ''
    # Option Information

    for interaction in PossibleActions:
        info += '\n[%s] %s' % (PossibleActions.index(interaction), interaction.infoString())

    return info


def generateInteractionsString(Section, LastInteractionInfo):
    # Gen Action String
    actStr = '[0] Back \n'
    # Loop
    for interaction, info in Section:
        actStr += '[' + str(Section.index(interaction)+1) + '] '
        actStr += Section.interactionType + ' ' + interaction
        actStr += ' for ' + str(info) + '\n'

    return actStr
