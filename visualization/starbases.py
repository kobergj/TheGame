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

    # Info Message
    to_print += "\nShip For Sale:"

    # Print Price
    to_print += "\n Price: %s" % Starbase.shipPrice

    # Loop through Shipstats
    for stat in Starbase.shipForSale.stats:
        new_ship = Starbase.shipForSale.stats[stat]
        current_ship = Player.currentShip.stats[stat]

        if new_ship >= current_ship:
            to_print += "\n [%s]: %s (+%s)" % (stat, new_ship, new_ship-current_ship)

        else:
            to_print += "\n [%s]: %s (%s)" % (stat, new_ship, new_ship-current_ship)

    to_print += "\n\n[0] Dont Buy Ship"
    choiceList.append('refuse')

    to_print += "\n[1] Buy Ship"
    choiceList.append('accept')

    # Print String
    print to_print

    # Await Players Choice
    choice = input()

    while choice not in range(len(choiceList)):
        choice = uvs.invalidChoice(choice)

    choice = choiceList[choice]

    return choice
