import database.database as db


def chooseNextDestination(Universe, Player):
    mapIdentifiers = db.Visualization.mapIdentifiers

    print '\n' * 100
    print "\n Choose Destination\n"

    print '###'*(len(Universe.Map[0])*2-1)

    choiceList = [False]

    for row in Universe.Map:
        for name in row:
            to_print = mapIdentifiers['Empty']

            if name:
                anomaly = Universe.anomalyList[name]
                to_print = mapIdentifiers[anomaly.__class__.__name__]

                if name in Player.currentShip.travelCosts:
                    if Player.currentShip.distances[name] == 0.0:
                        to_print = to_print.replace('00', str(0))
                        to_print = '->' + to_print
                    else:
                        choiceList.append(name)

                        to_print = to_print.replace('00', str(len(choiceList)-1))

                else:
                    to_print = to_print.replace('00', '')

            while len(to_print) < 4:
                to_print += ' '

            print to_print,

        print '\n',

    print '###'*(len(Universe.Map[0])*2-1)

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
