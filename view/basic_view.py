import configuration.log_details as log

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
                                    ' ENTER '
                                ],
                      'Current': [  'You are',
                                    '  Here '
                                ]
                      }

    def __init__(self, Universe):
        self.uvMatrix = self.drawMap(Universe)
        self._uvMatrix = self.uvMatrix[:]

        self.point_len = len(self.mapIdentifiers['Empty'])

    def __call__(self, view_model):
        log.log('Getting Windows Of %s' % view_model.__class__.__name__)
        windows, positions = mv.get_view(view_model, self.mapIdentifiers)

        log.log('Inserting %s at %s' % (windows, positions))
        self.window_inserter(windows, positions)

        print '\n' * 100
        print sv.stat_view(view_model.player)
        print iv.info_view(view_model.anomaly)
        print mv.mainframe_view(self.uvMatrix)

        choice = raw_input()

        self.uvMatrix = self._uvMatrix[:]

        while True:
            try:
                if choice == '':
                    choice = 0

                log.log('Player choose %s' % choice)
                result = view_model.choiceList[int(choice)]
                view_model.choice = result

            except ValueError:

                print 'Sorry, %s not valid. Please Press ENTER or valid number' % choice

                choice = raw_input()

            except IndexError:

                print 'Sorry, There is no Option %s' % choice

                choice = raw_input()

    def drawMap(self, Universe):
        # VizUniverse Map
        universeMatrix = list()

        # Loop through vertical Slices of Universe
        # log.log('drawing Map. Position: %s' % self.anomaly.coordinates)

        for verticalSlice in Universe.Map:
            row = list()

            # Loop through Anomalies
            for anomaly in verticalSlice:
                # Assume its Empty
                first_line = self.mapIdentifiers['Empty']
                second_line = self.mapIdentifiers['Empty']


                if anomaly:
                    first_line = self.mapIdentifiers['Unknown'][0]
                    second_line = self.mapIdentifiers['Unknown'][1]

                row.append([first_line, second_line])

            universeMatrix.append(row)

        return universeMatrix

    def window_inserter(self, window_list, position_list):

        for i, window in enumerate(window_list):
            log.log('Get Position')
            position = position_list[i]

            log.log('Convert String to Matrix')
            matrix = self.string2matrix(window)

            log.log('Calc Window Position')
            x_rng, y_rng = self.calculate_window_range(matrix, position)

            log.log('Insert Window')
            self.insert_window(matrix, [x_rng, y_rng])


    def calculate_window_range(self, matrix, position):

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

        y_range = [anm_y, end_row]
        x_range = [anm_x, end_point]

        return x_range, y_range


    def insert_window(self, matrix, position):

        matrix_y = 0

        for map_y in range(*position[1]):

            matrix_x = 0

            for map_x in range(*position[0]):

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


