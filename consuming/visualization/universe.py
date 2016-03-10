
def chooseNextDestination(Universe, Player):
    # Where to store them best?
    mapIdentifiers = {'Empty':      '    ',
                      'Planet':     '(00)',
                      'Spacegate':  '[00]',
                      'Starbase':   '$00$',
                      }

    print '\n' * 100
    print "\n Choose Destination\n"

    print ' ####'*(len(Universe.Map[0]))

    choiceList = [False]

    # Loop through Rows
    for row in Universe.Map:
        print '#',
        # Each Point contains Anomaly Name
        for anomalyName in row:
            # Assume its Empty
            to_print = mapIdentifiers['Empty']

            if anomalyName:
                # Load Anomaly
                anomaly = Universe.anomalyList[anomalyName]
                # Load Map Identifier
                to_print = mapIdentifiers[anomaly.__class__.__name__]

                # Check if Anomaly is current
                if Player.currentPosition == anomalyName:
                    to_print = to_print.replace('00', '')
                    # Add Location Arrow
                    to_print = '->' + to_print

                # Check if Anomaly is reachable
                elif anomalyName in Player.currentShip.travelCosts:
                    choiceList.append(anomalyName)

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

    currentAnomaly = Universe.anomalyList[Player.currentPosition]

    if currentAnomaly.enemies:
        emyatk = str(currentAnomaly.enemies[0].attackPower)
        emydef = str(currentAnomaly.enemies[0].shieldStrength)

        fight_or_land = 'Fight - Atk: %s, Def: %s ' % (emyatk, emydef)

        for enemy in currentAnomaly.enemies[1:]:
            fight_or_land += '+'

    else:
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

    next_dest = choiceList[choice]

    return next_dest


def invalidChoice(choice):
    print 'Sorry, %s not valid' % choice
    choice = input()

    return choice
