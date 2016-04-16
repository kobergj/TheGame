import logbook.configuration as log

def chooseNextDestination(Universe, Player, ActiveCoordinates, AvailableSections=None, TravelCosts=0):
    print '\n' * 100

    uvMap = drawMap(Universe, Player, ActiveCoordinates, TravelCosts)

    anomalyInfoString = anomalyInfo(Universe, Player, ActiveCoordinates)

    optionsString = showOptions(Universe, Player, ActiveCoordinates, TravelCosts)

    statsString = playerStats(Player)

    print statsString
    print uvMap
    print anomalyInfoString
    print optionsString

    choice = raw_input()

    options = {
        '': uvMap,
        '1': False
    }

    while True:
        try:
            result = options[choice]
            return result
        except KeyError:
            choice = invalidChoice(choice)




def drawMap(Universe, Player, ActiveCords, TravelCosts):
    # Where to store them best? 7   ' A12D12'
    mapIdentifiers = {'Empty':      '       ',
                      'Unknown':[   '       ',
                                    '   ?   ',
                                ],
                      'Planet':[    '  /Pl\ ',
                                    '  \__/ ',
                                    # '   ()  '
                                ],
                      'Spacegate':[ '   SG  ',
                                    '  /__\ ',
                                    # '   []  '
                                ],
                      'Starbase':[  '  |SB| ',
                                    '  |__| ',
                                    # '   $$  '
                                ]
                      }

    universeMap = '#######'*(len(Universe.Map[0])) + '##\n'

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

                # if not TravelCosts[anomaly.name]:
                #     first_line = mapIdentifiers['Unknown'][0]
                #     second_line = mapIdentifiers['Unknown'][1]

                # Check if Anomaly is Active
                if ActiveCords == anomaly.coordinates:
                    log.log('Active %s %s' % (anomaly.name, str(anomaly.coordinates)))
                    first_line = first_line.replace('   ', ' ->')
                    first_line = first_line.replace('  /', ' ->')
                    first_line = first_line.replace('  |', ' ->')
                    first_line = first_line.replace('\ ', '<-')
                    first_line = first_line.replace('| ', '<-')
                    first_line = first_line.replace('  ', '<-')

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

        universeMap += first_row + '\n'
        universeMap += second_row + '\n'
        # print third_row

    universeMap += '#######'*(len(Universe.Map[0])) + '##'

    return universeMap


def playerStats(Player):
    playerStatsTemplate ="""

    Current Stats:
    Credits: %(credits)s
    Attack:  %(attackPower)s    Defense: %(curDef)s/%(maxDef)s
    Maximum Travel Distance: %(maxTravelDistance)s         Maintenance Costs: %(maintCosts)s

    Cargo Bay: %(currentCargo)s/%(maxCargo)s
            %(inCargo)s

    Rooms:  CURRENTROOMS/MAXROOMS
            ROOMS"""

    playerStats = {
        'credits': Player.credits,
        'attackPower': Player.currentShip.attackPower(),
        'curDef': Player.currentShip.shieldStrength(),
        'maxDef': Player.currentShip.shieldStrength.startValue,
        'maxTravelDistance': Player.currentShip.maxTravelDistance(),
        'maintCosts': Player.currentShip.maintenanceCosts(),
        'currentCargo': Player.currentShip.cargoCapacity.startValue - Player.currentShip.cargoCapacity(),
        'maxCargo': Player.currentShip.cargoCapacity.startValue,
        'inCargo': Player.currentShip.inCargo
    }

    return playerStatsTemplate % playerStats



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

    return information


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

    finalString += "\n[1] Checkout Next Destination"

    return finalString


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
