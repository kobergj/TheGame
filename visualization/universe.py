import database.database as db


def chooseNextDestination(Universe, Player):
    mapIdentifiers = db.Visualization.mapIdentifiers

    print '\n' * 100
    print "\n Choose Destination\n"

    print '###'*(len(Universe.Map[0])*2-1)

    choiceList = list()

    for row in Universe.Map:
        for name in row:
            to_print = mapIdentifiers['Empty']

            if name:
                anomaly = Universe.anomalyList[name]
                to_print = mapIdentifiers[anomaly.__class__.__name__]

                if name in Player.currentShip.travelCosts:
                    choiceList.append(name)

                    to_print = to_print.replace('00', str(len(choiceList)))

                    if Player.currentShip.distances[name] == 0.0:
                        to_print = '->' + to_print

                else:
                    to_print = to_print.replace('00', '')

            while len(to_print) < 4:
                to_print += ' '

            print to_print,

        print '\n',

    print '###'*(len(Universe.Map[0])*2-1)

    for anomaly in choiceList:
        print "[%s] %s, distance: %s clicks, Cost: %s" % (choiceList.index(anomaly) + 1,
                                                          anomaly,
                                                          Player.currentShip.distances[anomaly],
                                                          Player.currentShip.travelCosts[anomaly])

    choice = input()

    while choice not in range(1, len(choiceList)+1):
        if choice == -1:
            print Universe.Map
            choice = 0
        else:
            choice = invalidChoice(choice)

    next_dest = choiceList[choice-1]

    return next_dest


def invalidChoice(choice):
    print 'Sorry, %s not valid' % choice
    choice = input()

    return choice
