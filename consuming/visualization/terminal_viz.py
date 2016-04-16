import logbook.configuration as log

class View:
    # Where to store them best? 7   '0123456'
    mapIdentifiers = {'Empty':      '       ',
                      'Unknown':[   '       ',
                                    '   ?   ',
                                ],
                      'Planet':[    '  /Pl\ ',
                                    '  \__/ ',
                                ],
                      'Spacegate':[ '   SG  ',
                                    '  /__\ ',
                                ],
                      'Starbase':[  '  |SB| ',
                                    '  |__| ',
                                ],
                      'Highlight':[ ' ->  <-',
                                    'Costs:%u'
                                ],
                      }

    playerStatsTemplate ="""

    Current Stats:
    Credits: %(credits)s    Attack:  %(attackPower)s    Defense: %(curDef)s/%(maxDef)s  Maximum Travel Distance: %(maxTravelDistance)s  Maintenance Costs: %(maintCosts)s

    Cargo Bay: %(currentCargo)s/%(maxCargo)s -> %(inCargo)s

    Rooms:  %(currentRooms)s/%(maxRooms)s -> %(roomList)s"""


    def __init__(self, Universe, Player):
        self.act_anmy = Universe[Player.currentPosition]

        self.uvMatrix = self.drawMap(Universe)

        self.point_len = len(self.mapIdentifiers['Empty'])

        self.playerStatsString = self.current_stats(Player)

        self.anomalyInfoLine = self.anomaly_info(self.act_anmy)

        self.detail_window = None

        self.window_position = self.act_anmy.coordinates

        self.choiceList = [None]

    def __call__(self):

        self.insertWindow(self.detail_window, self.window_position)

        print '\n' * 100
        print self.playerStatsString
        print self.anomalyInfoLine
        print self.showUniverse()

        choice = raw_input()

        while True:
            try:
                if choice == '':
                    choice = 0

                log.log('Player choose %s' % choice)
                result = self.choiceList[int(choice)]
                return result

            except ValueError:

                print 'Sorry, %s not valid. Please Press ENTER or valid number' % choice

                choice = raw_input()

            except IndexError:

                print 'Sorry, There is no Option %s' % choice

                choice = raw_input()


    def current_stats(self, Player):

        def cargoString(CargoBay):
            cargo_string = ''

            for good_name, amount in CargoBay.iteritems():
                cargo_string += "%s: %s  " % (good_name, amount)

            return cargo_string

        def roomString(Rooms):
            room_string = ''

            for room in Rooms:
                room_string += str(room.name)

                for statBoost in room.statBoosts:
                    room_string += '-%s:%+d' %(statBoost.statName, statBoost.startValue)

                room_string += ' -- '

            return room_string

        playerStats = {
            'credits': Player.credits,
            'attackPower': Player.currentShip.attackPower(),
            'curDef': Player.currentShip.shieldStrength(),
            'maxDef': Player.currentShip.shieldStrength.startValue,
            'maxTravelDistance': Player.currentShip.maxTravelDistance(),
            'maintCosts': Player.currentShip.maintenanceCosts(),
            'currentCargo': Player.currentShip.cargoCapacity.startValue - Player.currentShip.cargoCapacity(),
            'maxCargo': Player.currentShip.cargoCapacity.startValue,
            'inCargo': cargoString(Player.currentShip.inCargo),
            'currentRooms': Player.currentShip.spaceForRooms.startValue - Player.currentShip.spaceForRooms(),
            'maxRooms': Player.currentShip.spaceForRooms.startValue,
            'roomList': roomString(Player.currentShip.rooms)
        }

        return self.playerStatsTemplate % playerStats


    def anomaly_info(self, Anomaly):
        if not Anomaly:
            return ' '

        # Possible Interaction
        amyname = Anomaly.name
        amytype = Anomaly.__class__.__name__

        information = '%s %s ' % (amytype, amyname)

        for enemy in Anomaly.enemies:
            information += 'X'

        information += ' '

        # Buys It Goods?
        try:
            buy_information = '- Buys '

            for good in Anomaly.goodsConsumed:
                buy_information += '%s@%s ' % (good.name, good.price)

            buy_information += ' '

            information += buy_information
        except AttributeError:
            pass

        # Sells it Goods?
        try:
            sell_information = '- Sells: '

            for good in Anomaly.goodsProduced:
                sell_information += '%s@%s ' % (good.name, good.price)

            sell_information += ' '

            information += sell_information

        except AttributeError:
            pass

        return information

    def showUniverse(self):
        """Prints Universe Map. Highlights an Anomaly if given."""

        universeString = ''

        for y, row in enumerate(self.uvMatrix):
            first_line = ''
            second_line = ''

            for x, point in enumerate(row):

                first_line += point[0]
                second_line += point[1]

            universeString += first_line + '\n' + second_line + '\n'

        return universeString

    def drawMap(self, Universe):
        # VizUniverse Map
        universeMatrix = list()

        # Loop through vertical Slices of Universe
        log.log('drawing Map. Position: ' % self.act_anmy.coordinates)

        for verticalSlice in Universe.Map:
            row = list()

            # Loop through Anomalies
            for anomaly in verticalSlice:
                # Assume its Empty
                first_line = self.mapIdentifiers['Empty']
                second_line = self.mapIdentifiers['Empty']


                if anomaly:
                    # Load Map Identifier
                    anomalyType = anomaly.__class__.__name__

                    first_line = self.mapIdentifiers[anomalyType][0]
                    second_line = self.mapIdentifiers[anomalyType][1]

                    if self.act_anmy == anomaly:
                        log.log('Current %s' % str(anomaly.coordinates))
                        second_line = second_line.replace('__', 'XX')

                    if anomaly.travelCosts is None:
                        first_line = self.mapIdentifiers['Unknown'][0]
                        second_line = self.mapIdentifiers['Unknown'][1]

                row.append([first_line, second_line])

            universeMatrix.append(row)

        return universeMatrix


    def insertWindow(self, raw_info_string, position):

        matrix = self.string2matrix(raw_info_string)

        # Technical Approach
        anm_x = position[:][0]
        anm_y = position[:][1]

        # needed_rows = len(matrix)

        start_row = anm_y

        while start_row < 0:
            anm_y += 1
            start_row = anm_y

        end_row = start_row + len(matrix)

        while end_row >= len(self.uvMatrix):
            anm_y -= 1
            start_row = anm_y
            end_row = start_row + len(matrix)

        start_point = anm_x

        while start_point < 0:
            anm_x += 1
            start_point = anm_x

        end_point = start_point + len(matrix[0])

        while end_point >= len(self.uvMatrix[0]):
            anm_x -= 1
            start_point = anm_x
            end_point = start_point + len(matrix[0])

        row_new = 0

        for row_old in range(start_row, end_row):

            point_new = 0

            for point_old in range(start_point, end_point):
                try:
                    self.uvMatrix[row_old][point_old][0] = matrix[row_new][point_new]
                except IndexError:
                    self.uvMatrix[row_old][point_old][0] = ' ' * self.point_len

                point_new += 1

            row_new += 1

            point_new = 0

            for point_old in range(start_point, end_point):
                try:
                    self.uvMatrix[row_old][point_old][1] = matrix[row_new][point_new]
                except IndexError:
                    self.uvMatrix[row_old][point_old][1] = ' ' * self.point_len

                point_new += 1

            row_new += 1


    def string2matrix(self, rawString):
        row_splitted = rawString.split('\n')

        matrix = list()

        for row_string in row_splitted:

            row = list()

            while row_string:
                point = row_string[:self.point_len]

                row_string = row_string[self.point_len:]

                while len(point) < self.point_len:
                    point += ' '

                row.append(point)

            matrix.append(row)

        return matrix




class UniverseView(View):

    def __init__(self, Universe, Player, act_anmy):

        View.__init__(self, Universe, Player)

        self.detail_window = self.travel_details(act_anmy)

        self.window_position = act_anmy.coordinates

        self.choiceList = [True, False]

    def travel_details(self, anomaly):

        details = self.mapIdentifiers['Highlight'][0]

        details += '\n'

        details += self.mapIdentifiers['Highlight'][1] % anomaly.travelCosts

        return details


class AnomalyView(View):

    def __init__(self, Universe, Player, avail_secs):

        View.__init__(self, Universe, Player)

        self.detail_window = self.anomaly_details(avail_secs)

        self.choiceList = avail_secs

    def anomaly_details(self, availableSections):
        sectionInfo = 'Welcome to %s %s\n' % (self.act_anmy.__class__.__name__, self.act_anmy.name)
        for i, section in enumerate(availableSections):
            sectionInfo += " [%s] %s\n" % (i, section.infoString())

        return sectionInfo

class SectionView(View):

    def __init__(self, Universe, Player, active_sec):
        View.__init__(self, Universe, Player)

        self.detail_window = self.section_details(active_sec)

        self.choiceList = [None]

        for item in active_sec:
            self.choiceList.append(item)

    def section_details(self, Section):
        # Build Information
        interactionInfo = ''

        interactionInfo += "%s %s" % (self.act_anmy.__class__.__name__, self.act_anmy.name)

        interactionInfo += " -- %s\n"  % Section.infoString()

        interactionInfo += " [0] Back\n"

        for i, item in enumerate(Section):
            interactionInfo += " [%s] %s for %s\n" % (i+1, item.name, item.price)

        return interactionInfo


class Deprecated:
    def __call__(self, Player, active_sec=None, avail_secs=None, active_anmy=None):

        if active_sec:
            self.insertSectionDetails(active_sec)

            choiceList = [None]

            for item in active_sec:
                choiceList.append(item)

        elif avail_secs:
            self.insertAnomalySections(avail_secs)

            choiceList = avail_secs

        elif active_anmy:
            self.highlight_anomaly(active_anmy.coordinates)

            choiceList = [True, False]



    def insertSectionDetails(self, Section):
        raw_info_string = self.generateInteractionString(Section)

        self.insertWindowInMap(raw_info_string)

    def insertAnomalySections(self, AvailableSections):
        raw_info_string = self.generateSectionsString(AvailableSections)

        self.insertWindowInMap(raw_info_string)


    def highlight_anomaly(self, anomalyCords):

        for y, row in enumerate(self.uvMatrix):

            for x, point in enumerate(row):

                if anomalyCords == [x, y]:
                    self.uvMatrix[y][x][0] = self.highlight_line(self.uvMatrix[y][x][0])

    def highlight_line(self, line):
        highlighted_line = self.mapIdentifiers['Highlight']
        # to_replace = filter(lambda x: x.isalpha(), highlighted_line)

        # anomalyIdentifiers = filter(lambda x: x.isalpha(), line)

        # highlighted_line = highlighted_line.replace(to_replace, anomalyIdentifiers)

        return highlighted_line


