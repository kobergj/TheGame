import logbook.configuration as log

import view.infoframe_view as iv
import view.statframe_view as sv
import view.mainframe_view as mv

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
                      'Current': [  'You are',
                                    '  Here '
                                ]
                      }

    def __init__(self, Universe, Player):
        self.act_anmy = Universe[Player.currentPosition]

        self.uvMatrix = self.drawMap(Universe)

        self.point_len = len(self.mapIdentifiers['Empty'])

        self.detail_window = None

        self.window_position = self.act_anmy.coordinates

        self.choiceList = [None]

    def __call__(self, view_model):

        self.insertWindow(self.detail_window, self.window_position)

        print '\n' * 100
        print sv.StatView(view_model.player)
        print iv.InfoView(view_model.anomaly)
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



    def showUniverse(self):
        """Prints Universe Map. Highlights an Anomaly if given."""

        universeString = ''

        for y, row in enumerate(self.uvMatrix):
            first_line = ''
            second_line = ''

            for x, point in enumerate(row):

                log.log('Drawing %s' % point, level=10)
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
                        first_line = self.mapIdentifiers['Current'][0]
                        second_line = self.mapIdentifiers['Current'][1]

                    if anomaly.travelCosts is None:
                        first_line = self.mapIdentifiers['Unknown'][0]
                        second_line = self.mapIdentifiers['Unknown'][1]

                row.append([first_line, second_line])

            universeMatrix.append(row)

        return universeMatrix


    def insertWindow(self, raw_info_string, position):

        log.log('Convert String to Matrix')
        matrix = self.string2matrix(raw_info_string)
        log.log('Needed Rows: %s, Needed Points: %s' % (len(matrix), len(matrix[0])))

        log.log('Starting Coordinates %s' % position)
        anm_y = position[:][1]
        anm_x = position[:][0]

        # Should not happen
        while anm_y < 0:
            anm_y += 1

        # Calculate End Row Index
        end_row = anm_y + len(matrix)

        # Fit in Map?
        while end_row > len(self.uvMatrix):
            anm_y -= 1
            end_row = anm_y + len(matrix)

        # Should not happen
        while anm_x < 0:
            anm_x += 1

        # Calculate End Point Index
        end_point = anm_x + len(matrix[0])

        # Fit In Map?
        while end_point > len(self.uvMatrix[0]):
            anm_x -= 1
            end_point = anm_x + len(matrix[0])

        matrix_y = 0

        for map_y in range(anm_y, end_row):

            matrix_x = 0

            for map_x in range(anm_x, end_point):

                try:
                    point_one = matrix[matrix_y][matrix_x][0]

                except IndexError:
                    point_one = ' ' * self.point_len

                log.log('Overwriting %s with %s [%s]' % (
                                    self.uvMatrix[map_y][map_x][0], point_one, [map_x, map_y])
                                    )

                try:
                    point_two = matrix[matrix_y][matrix_x][1]
                     
                except IndexError:
                    point_two = ' ' * self.point_len

                log.log('Overwriting %s with %s' % (self.uvMatrix[map_y][map_x][1], point_two))

                self.uvMatrix[map_y][map_x] = [point_one, point_two]

                matrix_x += 1

            matrix_y += 1


    def string2matrix(self, rawString):
        row_splitted = rawString.split('\n')
        log.log('Splitted String to %s' % row_splitted)

        matrix = list()

        row_one_counter = 0
        row_two_counter = 1

        while row_two_counter <=len(row_splitted):

            row = list()

            row_one = list()

            try:
                row_string = row_splitted[row_one_counter]
            except IndexError:
                row_string = ''

            while True:
                point_one = row_string[:self.point_len]

                row_string = row_string[self.point_len:]

                while len(point_one) < self.point_len:
                    point_one += ' '

                row_one.append(point_one)

                if not row_string:
                    break

            row_two = list()

            try:
                row_string = row_splitted[row_two_counter]
            except IndexError:
                row_string = ''

            while True:
                point_two = row_string[:self.point_len]

                row_string = row_string[self.point_len:]

                while len(point_two) < self.point_len:
                    point_two += ' '

                row_two.append(point_two)

                if not row_string:
                    break

            log.log('Make same length: %s, %s' % (row_one, row_two), level=10)
            while len(row_one) < len(row_two):
                row_one.append(' ' * self.point_len)

            while len(row_two) < len(row_one):
                row_two.append(' ' * self.point_len)

            log.log('Zipping: %s, %s' % (row_one, row_two))
            for i, unn in enumerate(row_one):

                row.append([row_one[i], row_two[i]])

            row_one_counter += 2
            row_two_counter += 2

            matrix.append(row)

        log.log('Matrix Generated: %s' % matrix)
        return matrix


