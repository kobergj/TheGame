import visualization.universe as uvs


def starbaseArrival(Starbase, Player):

    # Initialize Print String
    to_print = ''

    # Flush Terminal
    to_print += '\n' * 100

    # Fancy Border
    to_print += "==" * 40

    # Starbase Informations
    to_print += "\n You are at Starbase %s" % Starbase.name
    # # show ship
    # to_print += "\nShip For Sale:"
    # # Shipstats
    # for stat in
    to_print += "\nRooms For Sale: %s" % Starbase.roomsForSale

    # # Player Informations
    # to_print += "\n\nCurrent Shipstats:\n"
    # for name, value in Player.currentShip.stats.iteritems():
    #     to_print += '       %s: %s' % (name, value)

    to_print += "\n\nCurrent Rooms: %s" % Player.currentShip.rooms
    to_print += "\nNumber of Credits: %s" % Player.credits

    # Possible Actions
    to_print += "\nPossible Actions:"

    choiceList = list()

    i = 0
    to_print += "\n[%s] Quit Game" % i
    choiceList.append('quit')
    i += 1

    if Starbase.shipForSale:
        to_print += "\n[%s] Inspect Ship" % i
        choiceList.append('inspectShip')
        i += 1

    to_print += "\n[%s] Inspect Rooms" % i
    choiceList.append('inspectRooms')
    i += 1

    to_print += "\n[%s] Depart" % i
    choiceList.append('depart')
    i += 1

    # Print String
    print to_print

    # Await Players Choice
    choice = input()

    while choice not in range(len(choiceList)):
        choice = uvs.invalidChoice(choice)

    choice = choiceList[choice]

    return choice


def buyShip(Starbase, Player):
    # Initialize
    to_print = ''
    choiceList = list()

    # Fancy Border
    to_print += "--" * 40

    # Info Message
    to_print += "\nShip For Sale:"

    # Print Price
    to_print += "\n Price: %s" % Starbase.shipForSale.price

    # Bad
    statList = ['cargoCapacity', 'maintenanceCosts', 'maxTravelDistance', 'spaceForRooms', 'attackPower',
                'shieldStrength']

    # Loop through Shipstats
    for stat in statList:
        new_ship = Starbase.shipForSale.__dict__[stat]
        current_ship = Player.currentShip.__dict__[stat]

        if new_ship >= current_ship:
            to_print += "\n [%s]: %s (+%s)" % (stat, new_ship, new_ship-current_ship)

        else:
            to_print += "\n [%s]: %s (%s)" % (stat, new_ship, new_ship-current_ship)

    to_print += "\n\n[0] Dont Buy Ship"
    choiceList.append('refuse')

    to_print += "\n[1] Buy Ship"
    choiceList.append('accept')

    # Print
    print to_print

    # Await Players Choice
    choice = input()

    while choice not in range(len(choiceList)):
        choice = uvs.invalidChoice(choice)

    choice = choiceList[choice]

    return choice


def buyRooms(Starbase, Player):
    to_print = ''

    for room in Starbase.roomsForSale:
        to_print += "\n %s" % room.name

        to_print += "\n  price: %s" % room.price

        for stat, value in room.statBoosts.iteritems():
            to_print += "\n  %s: +%s" % (stat, str(value))

        to_print += '\n'

    print to_print

    raw_input()
