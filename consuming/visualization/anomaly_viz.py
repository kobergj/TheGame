# DEPRECATED


# def chooseSection(Anomaly, Player, AvailSecs, UniMap):
#     # Flush Terminal
#     print '\n' * 100

#     newMap = addInteractionInfo(UniMap, Anomaly, availSecs=AvailSecs)

#     print newMap

#     choice = raw_input()

#     while True:
#         try:
#             result = AvailSecs[int(choice)]
#             return result
#         except ValueError:
#             choice = invalidChoice(choice)


# def chooseInteraction(Anomaly, Player, Section, UniMap):
#     # Flush Terminal
#     print '\n' * 100

#     newMap = addSubsectionInfo(UniMap, Anomaly, Section)

#     print newMap

#     choice = raw_input()

#     while True:
#         try:
#             choice = int(choice)
#             if choice == 0:
#                 return
#             result = Section[choice-1]
#             return result
#         except ValueError:
#             choice = invalidChoice(choice)



# def addSubsectionInfo(UniMap, Anomaly, ActiveSection):
#     universemap = UniMap.split('\n')


#     for vertSlice in universemap:
#         if 'XX' in vertSlice:
#             centerSliceNumber = universemap.index(vertSlice)

#             splitted = vertSlice.split('XX')

#             centerPoint = len(splitted[0]) - 4

#             break

#     # Build Information
#     info = list()

#     anInfo = "%s %s" % (Anomaly.__class__.__name__, Anomaly.name)

#     anInfo += " -- %s"  % ActiveSection.infoString()

#     info.append(anInfo)


#     interactionInfo = " [0] Back"
#     info.append(interactionInfo)

#     for item, price in ActiveSection:
#         interactionInfo = " [%s] %s for %s" % (ActiveSection.index(item)+1, item, price)
#         info.append(interactionInfo)

#     line = centerSliceNumber - len(info) / 2

#     for detail in info:
#         new_line = fitInLine(detail, universemap[line], centerPoint)
#         universemap[line] = new_line
#         line += 1

#     final = ''
#     for sl in universemap:
#         final += sl + '\n'

#     return final



# def addInteractionInfo(UniMap, Anomaly, availSecs=None, activeSection=None):
#     universemap = UniMap.split('\n')


#     for vertSlice in universemap:
#         if 'XX' in vertSlice:
#             centerSliceNumber = universemap.index(vertSlice)

#             splitted = vertSlice.split('XX')

#             centerPoint = len(splitted[0]) - 4

#             break

#     # Build Information
#     info = list()

#     anInfo = "%s %s" % (Anomaly.__class__.__name__, Anomaly.name)

#     if activeSection:
#         anInfo += " -- %s"  % activeSection.infoString()

#     info.append(anInfo)

#     # for enemy in Anomaly.enemies:
#     #     enemy_info = "Enemy: Atk:%s Def:%s" % (enemy.attackPower, enemy.shieldStrength)
#     #     info.append(enemy_info)

#     if activeSection:
#         interactionInfo = " [0] Back"
#         info.append(interactionInfo)
#         for item, price in activeSection:
#             interactionInfo = " [%s] %s for %s" % (activeSection.index(item)+1, item, price)
#             info.append(interactionInfo)

#     else:
#         for section in availSecs:
#             sectionInfo = " [%s] %s" % (availSecs.index(section), section.infoString())
#             info.append(sectionInfo)

#     line = centerSliceNumber - len(info) / 2

#     for detail in info:
#         new_line = fitInLine(detail, universemap[line], centerPoint)
#         universemap[line] = new_line
#         line += 1

#     final = ''
#     for sl in universemap:
#         final += sl + '\n'

#     return final


# def fitInLine(toFit, Line, StartingIndex):
#     left = Line[:StartingIndex]

#     left += toFit + Line[StartingIndex+len(toFit):]

#     return left


# #####  DEPRECATED #######

# def OLDchooseSection(Anomaly, Player, AvailableSections):
#     # Flush Terminal
#     print '\n' * 100

#     # Border
#     print '--' * 40

#     # Information Screen
#     information = generateInfoString(Anomaly, Player, AvailableSections=AvailableSections)
#     print information

#     # Border
#     print '--' * 40

#     # Await Choice
#     choice = raw_input()

#     while True:

#         if choice == '':
#             return AvailableSections[-1]

#         try:
#             choice = int(choice)

#             # Not Valid Choice
#             if choice not in range(len(AvailableSections)):
#                 raise ValueError

#             return AvailableSections[choice]

#         except ValueError:
#             print "Sorry %s not valid" % choice
#             choice = raw_input()



# def OLDchooseInteraction(Anomaly, Player, Section, LastInteractionInfo):
#     # Margin
#     print '\n'*100
#     # Border
#     print '--' * 40

#     # Gen Section Info
#     secinfo = generateInfoString(Anomaly, Player, Section, LastInteractionInfo)
#     print secinfo

#     # Border
#     print '--' * 40

#     # Await Choice
#     choice = raw_input()

#     while True:
#         if choice == '':
#             if LastInteractionInfo != True:
#                 number = Section.index(LastInteractionInfo)

#                 return Section[number]

#             return

#         try:
#             formatedChoice = int(choice)

#             if formatedChoice not in range(len(Section)+1):
#                 raise ValueError

#             if formatedChoice == 0:
#                 return

#             return Section[formatedChoice-1]

#         except ValueError:
#             print "Sorry %s not valid" % choice
#             choice = raw_input()


# def generateInfoString(Anomaly, Player, Section=True, LastInteractionInfo=None, AvailableSections=None):
#     # Anomaly Type
#     anomalyType = Anomaly.__class__.__name__
#     # Init
#     info = ''
#     # Positonal Information
#     info += "\n You are at %s %s" % (anomalyType, Anomaly.name)

#     longInfo = """
#         Current Stats:
#             Credits: CREDS
#             Attack:  ATTACK    Defense: DEFCURR/DEFMAX
#             Maximum Travel Distance: TRAVELDIST
#             Maintenance Costs: MAINTCOST

#             Cargo Bay: CURRENTCARGO/MAXCARGO -> INCARGO

#             Rooms:  CURRENTROOMS/MAXROOMS
#                     ROOMS

#         You are at ANOMALYTYPE ANOMALYNAME
#     """

#     longInfo = longInfo.replace('ANOMALYTYPE', anomalyType)

#     longInfo = longInfo.replace('ANOMALYNAME', Anomaly.name)

#     longInfo = longInfo.replace('CREDS', str(Player.credits))

#     longInfo = longInfo.replace('CURRENTCARGO', str(Player.currentShip.cargoCapacity.startValue - Player.currentShip.cargoCapacity()))

#     longInfo = longInfo.replace('MAXCARGO', str(Player.currentShip.cargoCapacity.startValue))

#     longInfo = longInfo.replace('INCARGO', str(Player.currentShip.inCargo))

#     longInfo = longInfo.replace('ATTACK', str(Player.currentShip.attackPower()))

#     longInfo = longInfo.replace('DEFCURR', str(Player.currentShip.shieldStrength()))

#     longInfo = longInfo.replace('DEFMAX', str(Player.currentShip.shieldStrength.startValue))

#     longInfo = longInfo.replace('TRAVELDIST', str(Player.currentShip.maxTravelDistance()))

#     longInfo = longInfo.replace('MAINTCOST', str(Player.currentShip.maintenanceCosts()))

#     longInfo = longInfo.replace('CURRENTROOMS', str(Player.currentShip.spaceForRooms.startValue - Player.currentShip.spaceForRooms()))

#     longInfo = longInfo.replace('MAXROOMS', str(Player.currentShip.spaceForRooms.startValue))

#     roomString = ''
#     for room in Player.currentShip.rooms:
#         roomString += room.name + '  '
#         for stat in room.statBoosts:
#             roomString += stat.statName + ' ' + str(stat.startValue) + '  '
#         roomString += '\n                    '

#     longInfo = longInfo.replace('ROOMS', roomString)

#     # Add Options
#     if Section == True:
#         longInfo += generateSectionsString(AvailableSections)
#     else:
#         longInfo += '\n\n\n'

#     # Add Goods Produced
#     try:
#         infoExtension = """
#         Merchant - Sells Goods:
#             GOODSFORSALEINFO
#         """

#         goodsSaleInfo = ''
#         for good in Anomaly.goodsProduced:
#             goodsInfo = "< GOODNAME: GOODPRICE >  "

#             goodsInfo = goodsInfo.replace('GOODNAME', good)

#             goodsInfo = goodsInfo.replace('GOODPRICE', str(Anomaly.prices[good]))

#             goodsSaleInfo += goodsInfo

#         infoExtension = infoExtension.replace('GOODSFORSALEINFO', goodsSaleInfo)

#         longInfo += infoExtension

#         if Section.__class__.__name__ == 'Merchant':
#             longInfo += generateInteractionsString(Section, LastInteractionInfo)
#         else:
#             longInfo += '\n\n'

#     except AttributeError:
#         pass

#     # Add Goods Consumed
#     try:
#         infoExtension = """
#         Trader - Buys Goods:
#             GOODSBUYINFO
#         """

#         goodsBuyInfo = ''
#         for good in Anomaly.goodsConsumed:
#             goodsInfo = "< GOODNAME: GOODPRICE >  "

#             goodsInfo = goodsInfo.replace('GOODNAME', good)

#             goodsInfo = goodsInfo.replace('GOODPRICE', str(Anomaly.prices[good]))

#             goodsBuyInfo += goodsInfo

#         infoExtension = infoExtension.replace('GOODSBUYINFO', goodsBuyInfo)

#         longInfo += infoExtension

#         if Section.__class__.__name__ == 'Trader':
#             longInfo += generateInteractionsString(Section, LastInteractionInfo)
#         else:
#             longInfo += '\n\n'

#     except AttributeError:
#         pass


#     # Add Rooms For Sale
#     try:
#         roomSaleInfo = """      Equipment Dealer - Sells Rooms: \n"""
#         for room in Anomaly.roomsForSale:
#             roomInfo = """              ROOMNAME: Price: PRICE """

#             roomInfo = roomInfo.replace('ROOMNAME', room.name)

#             roomInfo = roomInfo.replace('PRICE', str(room.price))

#             for statBoost in room.statBoosts:
#                 roomInfo += "/ STATNAME: STATVALUE "

#                 roomInfo = roomInfo.replace('STATNAME', statBoost.statName)

#                 roomInfo = roomInfo.replace('STATVALUE', str(statBoost.startValue))

#             roomInfo += '\n'

#             roomSaleInfo += roomInfo

#         longInfo += roomSaleInfo

#         if Section.__class__.__name__ == 'EquipmentDealer':
#             longInfo += generateInteractionsString(Section, LastInteractionInfo)

#     except AttributeError:
#         pass

#     return longInfo


# def generateSectionsString(PossibleActions):
#     # Init
#     info = '\n          '
#     # Option Information

#     for interaction in PossibleActions:
#         number = PossibleActions.index(interaction)

#         if number == len(PossibleActions)-1:
#             number = 'ENTER'

#         info += '/ [%s] %s /' % (str(number), interaction.__class__.__name__)

#     info += '\n \n'

#     return info


# def generateInteractionsString(Section, LastInteractionInfo):
#     # Gen Action String
#     actStr = """
#             / [0] Back /"""

#     if LastInteractionInfo == True:
#         actStr = actStr.replace('0', 'ENTER')
#     # Loop
#     for interaction, info in Section:
#         number = str(Section.index(interaction)+1)
#         if LastInteractionInfo == interaction:
#             number = 'ENTER'
#         actStr += '/ [' + number + '] '

#         actStr += Section.interactionType + ' ' + interaction

#         # actStr += ' for ' + str(info) + ' /'
#         actStr += ' /'

#     actStr += '\n'

#     return actStr

# def invalidChoice(choice):
#     print 'Sorry, %s not valid' % choice
#     choice = input()

#     return choice



# # TESTING SECTION

# class AnomalyScreen():

#     playerStatsTemplate ="""

#     Current Stats:
#     Credits: %(credits)s
#     Attack:  %(attackPower)s    Defense: %(curDef)s/%(maxDef)s
#     Maximum Travel Distance: %(maxTravelDistance)s         Maintenance Costs: %(maintCosts)s

#     Cargo Bay: %(currentCargo)s/%(maxCargo)s
#             %(inCargo)s

#     Rooms:  CURRENTROOMS/MAXROOMS
#             ROOMS"""

#     sectionTemplate = """

#     [%(num)s] %(sectionName)s"""  # -- %(sectionDescr)s""" 

#     subSectionTemplate = """
#         [%(num)s] %(item)s for %(price)s"""
#             # %(itemstats)s"""

#     backTemplate = """
#         [0] Back"""

#     def __init__(self, Player, AvailSections, activeSection=None):

#         playerStats = {
#             'credits': Player.credits,
#             'attackPower': Player.currentShip.attackPower(),
#             'curDef': Player.currentShip.shieldStrength(),
#             'maxDef': Player.currentShip.shieldStrength.startValue,
#             'maxTravelDistance': Player.currentShip.maxTravelDistance(),
#             'maintCosts': Player.currentShip.maintenanceCosts(),
#             'currentCargo': Player.currentShip.cargoCapacity.startValue - Player.currentShip.cargoCapacity(),
#             'maxCargo': Player.currentShip.cargoCapacity.startValue,
#             'inCargo': Player.currentShip.inCargo
#         }

#         InfoScreen = self.playerStatsTemplate % playerStats

#         for section in AvailSections:
#             idNumber = AvailSections.index(section)

#             if activeSection:
#                 idNumber = ''

#             sectionStats = {
#                 'num': idNumber,
#                 'sectionName': section.infoString(),
#             }

#             InfoScreen += self.sectionTemplate % sectionStats

#             if section:
#                 InfoScreen += self.backTemplate

#             for option, price in section:
#                 idNumber = ''

#                 if activeSection == section:
#                     idNumber = section.index(option)+1

#                 optionStats = {
#                     'num': idNumber,
#                     'item': option,
#                     'price': price,
#                     # 'itemstats': option.stats
#                 }
#                 InfoScreen += self.subSectionTemplate % optionStats

#         self.currentScreen = InfoScreen
#         self.availableSections = AvailSections

#     def show(self, Section=None):
#         # Flush Terminal
#         print '\n'*100

#         print self.currentScreen

#         choice = input()

#         if choice == 0:
#             return

#         if not Section:
#             return self.availableSections[choice-1]

#         return Section[choice]



# def planetScreen(Planet):

#     planetViz = """
#           %s %s
#             | %s %s
#             |   | %s %s
#             |   |   |          %s %s
#             |   |   |            \    %s %s
#             |   |   |             \     |    %s %s
#            [1] [2] [3]             \    |     /
# |-|      /----------------\      __[4]_[5]_[6]__     _       _
# | ||-|  | Goods For Sale  |    / Buys Goods       /   _ | _  _  | [7] Depart
# | || |  |  Merchant       |   / Trader           /    | | |  |  | Spaceport
# -----------------------------------------------------------------------------

# """
#     values = list()
#     indexes = list()
#     i = 1

#     for good in Planet.goodsProduced:
#         values.extend([good, Planet.prices[good]])
#         indexes.append(i)
#         i += 1

#     while len(values) < 6:
#         values.extend(['', ''])
#         indexes.append('')

#     for good in Planet.goodsConsumed:
#         values.extend([good, Planet.prices[good]])
#         indexes.append(i)
#         i += 1

#     while len(values) < 12:
#         values.extend(['', ''])
#         indexes.append('')

#     indexes.append(i)

#     # values.extend(indexes)

#     print planetViz % tuple(values)

#     raw_input()