import visualization.universe as uvs


def starbaseArrival(Starbase, Player):
    # Initialize Print String
    to_print = ''

    # Flush Terminal
    to_print += '\n' * 100

    # Fancy Border
    to_print += "==" * 40

    # Planet Informations
    to_print += "\n You are at Starbase %s" % Starbase.name
    to_print += "\nShip For Sale: %s" % Starbase.shipForSale
    to_print += "\nRooms For Sale: %s" % Starbase.roomsForSale

    # Player Informations
    to_print += "\n\nCurrent Shipstats:\n"
    for name, value in Player.currentShip.stats.iteritems():
        to_print += '       %s: %s' % (name, value)

    to_print += "\n\nCurrent Rooms: %s" % Player.currentShip.rooms
    to_print += "\nNumber of Credits: %s" % Player.credits

    # Possible Actions
    to_print += "\nPossible Actions:"

    choiceList = list()

    to_print += "\n[0] Quit Game"
    choiceList.append('quit')

    to_print += "\n[1] Inspect Ship"
    choiceList.append('inspectShip')

    to_print += "\n[2] Depart"
    choiceList.append('depart')

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
