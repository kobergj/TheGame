
def chooseNextDestination(Universe, Player, ActiveCoordinates=None, TravelCosts=0):
    print '\n' * 100
    print "\n Choose Destination\n"

    if not ActiveCoordinates:
        ActiveCoordinates = Player.currentPosition

    drawMap(Universe, Player, ActiveCoordinates)

    showOptions(Universe, Player, ActiveCoordinates, TravelCosts)

    choice = raw_input()

    # Wait for Landing Sequence
    while choice != '':

        # Show Next Destination
        if choice == '1':
            return

        # Invalid Choice
        else:
            choice = invalidChoice(choice)

    return True


def drawMap(Universe, Player, ActiveCords):
    # Where to store them best?
    mapIdentifiers = {'Empty':      '    ',
                      'Planet':     '()',
                      'Spacegate':  '[]',
                      'Starbase':   '$$',
                      }

    print ' ####'*(len(Universe.Map[0]))

    # Loop through vertical Slices of Universe
    for verticalSlice in Universe.Map:
        print '#',
        # Loop through Anomalies
        for anomaly in verticalSlice:
            # Assume its Empty
            to_print = mapIdentifiers['Empty']

            if anomaly:
                # Load Map Identifier
                to_print = mapIdentifiers[anomaly.__class__.__name__]

                # Check if Anomaly is Current
                if Player.currentPosition == anomaly.coordinates:
                    # to_print = to_print.replace('00', '')
                    # Add Location Arrow
                    to_print = '->' + to_print
                # Or Active
                elif ActiveCords == anomaly.coordinates:
                    # to_print = to_print.replace('00', '')
                    # Add Location Arrow
                    to_print = ' >' + to_print
                # Or else
                else:
                    to_print = '  ' + to_print  # + ' '

            print to_print,

        print '#\n',

    print ' ####'*(len(Universe.Map[0]))

    return


def showOptions(Universe, Player, DestinationCoordinates, TravelCosts):
    # Call Anomaly
    anomaly = Universe[DestinationCoordinates]
    # Init Info String
    finalString = '[ENTER] '
    # genrate Information Sting
    infoString = travelString(anomaly, TravelCosts)

    # Override if Interaction Possible
    if anomaly.coordinates == Player.currentPosition:
        infoString = interactionString(anomaly)

    finalString += infoString

    print finalString
    print "[1] Checkout Next Destination"


def interactionString(Anomaly):
    if Anomaly.enemies:
        # Possible Fight
        emyatk = str(Anomaly.enemies[0].attackPower())
        emydef = str(Anomaly.enemies[0].shieldStrength())

        fight_or_land = 'Fight - Atk: %s, Def: %s ' % (emyatk, emydef)

        for enemy in Anomaly.enemies[1:]:
            fight_or_land += '+'

    else:
        # Possible Interaction
        amyname = Anomaly.name
        amytype = Anomaly.__class__.__name__

        fight_or_land = '%s %s ' % (amytype, amyname)

        if amytype == 'Planet':
            fight_or_land += '- Buys '

            for good in Anomaly.goodsConsumed:
                fight_or_land += '%s@%s ' % (good[:2], str(Anomaly.prices[good]))

            fight_or_land += '- Sells: '

            for good in Anomaly.goodsProduced:
                fight_or_land += '%s@%s ' % (good[:2], str(Anomaly.prices[good]))

        if amytype == 'Spacegate':
            fight_or_land += '- Cost For Use: %s' % str(Anomaly.costForUse)

    return fight_or_land


def travelString(Anomaly, TravelCosts):
    tr_string = 'Fly to %s. Costs: %s' % (Anomaly.name, str(TravelCosts))

    return tr_string


def invalidChoice(choice):
    print 'Sorry, %s not valid' % choice
    choice = input()

    return choice
