def chooseNextDestination(Universe, Player):
    print "\n Choose Destination\n"

    print '###'*len(Universe.Map[0])

    choiceList = list()

    for row in Universe.Map:
        for name in row:

            if name == '':
                print '  ',

            else:
                if name in Player.currentShip.travelCosts:
                    choiceList.append(name)

                    if name in Universe.planetList:
                        idString = ' %s ' % str(len(choiceList))
                    elif name in Universe.spacegateList:
                        idString = '[%s]' % str(len(choiceList))

                    if Player.currentShip.distances[name] == 0.0:
                        idString = '(%s)' % idString
                    else:
                        idString = ' %s ' % idString

                    print idString,

                else:
                    print ' ' + name[:2] + ' ',
        print '\n',

    print '###'*len(Universe.Map[0])

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
