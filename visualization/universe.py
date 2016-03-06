
def chooseNextDestination(Universe, Player):
    # Where to store them best?
    mapIdentifiers = {'Empty':      '    ',
                      'Planet':     '(00)',
                      'Spacegate':  '[00]',
                      'Starbase':   '$00$',
                      }

    print '\n' * 100
    print "\n Choose Destination\n"

    print '####'*(len(Universe.Map[0]))

    choiceList = [False]

    # Loop through Rows
    for row in Universe.Map:
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
                    to_print = to_print.replace('00', str(0))
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

        print '\n',

    print '####'*(len(Universe.Map[0]))

    currentAnomaly = Universe.anomalyList[Player.currentPosition]

    if currentAnomaly.enemies:
        fight_or_land = 'Fight'
    else:
        fight_or_land = 'Land'

    print "[0]  -- " + fight_or_land + " -- "
    print "[99] -- Show TravelInfos --"

    choice = input()

    if choice == 99:
        for anomaly in choiceList[1:]:
            print "[%s] %s, distance: %s clicks, Cost: %s" % (choiceList.index(anomaly),
                                                              anomaly,
                                                              Player.currentShip.distances[anomaly],
                                                              Player.currentShip.travelCosts[anomaly])

        choice = input()

    while choice not in range(len(choiceList)+1):
        choice = invalidChoice(choice)

    next_dest = choiceList[choice]

    return next_dest


def invalidChoice(choice):
    print 'Sorry, %s not valid' % choice
    choice = input()

    return choice
