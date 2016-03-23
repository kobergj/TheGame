import logbook.configuration as log

def chooseNextDestination(Universe, Player, ActiveCoordinates, TravelCosts=0):
    print '\n' * 100
    print "\n Choose Destination\n"

    drawMap(Universe, Player, ActiveCoordinates, TravelCosts)

    anomalyInfo(Universe, Player, ActiveCoordinates)

    showOptions(Universe, Player, ActiveCoordinates, TravelCosts)

    choice = raw_input()

    # Wait for Landing Sequence
    while choice != '':

        # Show Next Destination
        if choice == '1':
            return False

        # Invalid Choice
        else:
            choice = invalidChoice(choice)

    return True


def drawMap(Universe, Player, ActiveCords, TravelCosts):
    # Where to store them best? 7   ' A12D12'
    mapIdentifiers = {'Empty':      '       ',
                      'Planet':[    '  /Pl\ ',
                                    '  \__/ ',
                                    # '   ()  '
                                ],
                      'Spacegate':[ '  /SG\ ',
                                    '  \__/ ',
                                    # '   []  '
                                ],
                      'Starbase':[  '  /SB\ ',
                                    '  \__/ ',
                                    # '   $$  '
                                ]
                      }

    print '#######'*(len(Universe.Map[0])) + '##'

    # Loop through vertical Slices of Universe
    log.log('drawing Map')
    for verticalSlice in Universe.Map:
        first_row = '# '
        second_row = '# '
        # third_row = '# '
        # Loop through Anomalies
        for anomaly in verticalSlice:
            # Assume its Empty
            first_line = mapIdentifiers['Empty']
            second_line = mapIdentifiers['Empty']
            # third_line = mapIdentifiers['Empty']

            if anomaly:
                # Load Map Identifier
                anomalyType = anomaly.__class__.__name__

                first_line = mapIdentifiers[anomalyType][0]
                second_line = mapIdentifiers[anomalyType][1]
                # third_line = mapIdentifiers[anomalyType][2]

                # Check if Anomaly is Active
                if ActiveCords == anomaly.coordinates:
                    log.log('Active %s %s' % (anomaly.name, str(anomaly.coordinates)))
                    first_line = first_line.replace(' /', '->')
                    first_line = first_line.replace('\ ', '<-')

                    # Third Line Goods For Sell
                    # try:
                    #     availableGoods = anomaly.goodsConsumed
                    #     third_line = ''
                    #     for good in availableGoods:
                    #         price = anomaly.prices[good]

                    #         third_line += '%s%s' % (good[:2], str(price))
                    # except AttributeError:
                    #     third_line = mapIdentifiers['Empty']

                if Player.currentPosition == anomaly.coordinates:
                    log.log('Current %s' % str(anomaly.coordinates))
                    second_line = second_line.replace('__', 'XX')

                while len(first_line) < 7:
                    first_line += ' '

                while len(second_line) < 7:
                    second_line += ' '

                # while len(third_line) < 7:
                #     third_line += ' '

            first_row += first_line
            second_row += second_line
            # third_row += third_line

        first_row += '#'
        second_row += '#'

        print first_row
        print second_row
        # print third_row

    print '#######'*(len(Universe.Map[0])) + '##'

    return


def anomalyInfo(Universe, Player, ActiveCoordinates):
    anomaly = Universe[ActiveCoordinates]
    # Possible Interaction
    amyname = anomaly.name
    amytype = anomaly.__class__.__name__

    information = '%s %s ' % (amytype, amyname)

    for enemy in anomaly.enemies:
        information += 'X'

    information += ' '

    # Buys It Goods?
    try:
        buy_information = '- Buys '

        for good in anomaly.goodsConsumed:
            buy_information += '%s@%s ' % (good[:2], str(anomaly.prices[good]))

        buy_information += ' '

        information += buy_information
    except AttributeError:
        pass

    # Sells it Goods?
    try:
        sell_information = '- Sells: '

        for good in anomaly.goodsProduced:
            sell_information += '%s@%s ' % (good[:2], str(anomaly.prices[good]))

        sell_information += ' '

        information += sell_information

    except AttributeError:
        pass

    print information


def showOptions(Universe, Player, DestinationCoordinates, TravelCosts):
    # Call Anomaly
    anomaly = Universe[DestinationCoordinates]
    # Init Info String
    finalString = '[ENTER] '
    # genrate Information Sting
    infoString = travelString(anomaly, TravelCosts)

    # Override if Interaction Possible
    if anomaly.coordinates == Player.currentPosition:
        infoString = 'Land'

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
