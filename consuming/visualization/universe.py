
def chooseNextDestination(Universe, Player):
    print '\n' * 100
    print "\n Choose Destination\n"

    choiceList = drawMap(Universe, Player)

    showOptions(Universe, Player)

    choice = raw_input()

    if choice == '':
        choice = 0

    if choice == '99':
        for anomaly in choiceList[1:]:
            print "[%s] %s, Cost For Travel: %s" % (choiceList.index(anomaly),
                                                    anomaly,
                                                    Player.currentShip.travelCosts[anomaly]
                                                    )

        choice = input()

    choice = int(choice)

    while choice not in range(len(choiceList)+1):
        choice = invalidChoice(choice)

    next_dest_coordinates = choiceList[choice]

    return next_dest_coordinates


def drawMap(Universe, Player):
    # Where to store them best?
    mapIdentifiers = {'Empty':      '    ',
                      'Planet':     '(00)',
                      'Spacegate':  '[00]',
                      'Starbase':   '$00$',
                      }

    print ' ####'*(len(Universe.Map[0]))

    choiceList = [False]

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

                # Check if Anomaly is current
                if Player.currentPosition == anomaly.coordinates:
                    to_print = to_print.replace('00', '')
                    # Add Location Arrow
                    to_print = '->' + to_print

                # Get Costs For Travel
                reachable = Player.currentShip.travelCosts[anomaly.name]

                # Check if reachable
                if reachable:
                    choiceList.append(anomaly.coordinates)

                    to_print = to_print.replace('00', str(len(choiceList)-1))

                # Not Reachable
                else:
                    to_print = to_print.replace('00', '')

                    to_print = ' ' + to_print + ' '

            while len(to_print) < 4:
                to_print += ' '

            print to_print,

        print '#\n',

    print ' ####'*(len(Universe.Map[0]))

    return choiceList


def showOptions(Universe, Player):
    currentAnomaly = Universe.callAnomaly(Player.currentPosition)

    if currentAnomaly.enemies:
        # Possible Fight
        emyatk = str(currentAnomaly.enemies[0].attackPower)
        emydef = str(currentAnomaly.enemies[0].shieldStrength)

        fight_or_land = 'Fight - Atk: %s, Def: %s ' % (emyatk, emydef)

        for enemy in currentAnomaly.enemies[1:]:
            fight_or_land += '+'

    else:
        # Possible Interaction
        amyname = currentAnomaly.name
        amytype = currentAnomaly.__class__.__name__

        fight_or_land = '%s %s ' % (amytype, amyname)

        if amytype == 'Planet':
            fight_or_land += '- Buys '

            for good in currentAnomaly.goodsConsumed:
                fight_or_land += '%s@%s ' % (good[:2], str(currentAnomaly.prices[good]))

            fight_or_land += '- Sells: '

            for good in currentAnomaly.goodsProduced:
                fight_or_land += '%s@%s ' % (good[:2], str(currentAnomaly.prices[good]))

        if amytype == 'Spacegate':
            fight_or_land += '- Cost For Use: %s' % str(currentAnomaly.costForUse)

    print "[ENTER] " + fight_or_land
    print "[99] -- Show TravelInfos --"


def invalidChoice(choice):
    print 'Sorry, %s not valid' % choice
    choice = input()

    return choice
