def chooseNextDestination(Universe, Player):
    print "\n Choose Destination\n"

    print '###'*len(Universe.Map[0])

    i = 1
    choiceList = list()

    for row in Universe.Map:
        for identifier in row:

            if identifier == '':
                print '  ',

            else:
                if identifier in Player.currentShip.travelCosts:
                    print i, ' ',
                    choiceList.append(identifier)
                    i += 1

                else:
                    print identifier[:2],
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
