import copy

import logging

import gameinfo_view as gv
import infoframe_view as iv
import statframe_view as sv
import mainframe_view as mv

log = logging.getLogger('view')

class View:
    # Where to store them best? 7   '01234567890'

    def __init__(self, database):
        self.view_db = database.TerminalView

        self.uvMatrix = self.drawMap(database.StartConfiguration)
        self._uvMatrix = copy.deepcopy(self.uvMatrix)

        self.point_len = len(self.view_db.MapIdentifiers['Empty'])
        self.map_len = len(self.uvMatrix[0]) * self.point_len

    def __call__(self, view_model):
        log.info('Getting Windows Of %s' % view_model.__class__.__name__)
        windows, positions = mv.get_view(view_model, self.view_db)

        log.info('Inserting %s at %s' % (windows, positions))
        self.window_inserter(windows, positions)

        # Game Frame
        ga_view = gv.gameinfo_view(view_model, db=self.view_db)
        # Stat Frame
        pl_view = sv.stat_view(view_model.player, db=self.view_db)
        # Anm Frame
        anm_view = iv.info_view(view_model.anomaly, db=self.view_db)
        # Universe Frame
        uv_view = mv.mainframe_view(self.uvMatrix, db=self.view_db)

        log.info('Adding borders to %s' % [pl_view, anm_view, uv_view])
        complete_view = self.border(ga_view, pl_view, anm_view, uv_view, db=self.view_db)

        print '\n' * 100
        print complete_view

        choice = raw_input()
        log.info('Player choose %s' % choice)

        self.uvMatrix = copy.deepcopy(self._uvMatrix)

        while True:
            try:
                if choice == 'q':
                    log.info('Kill Flag. Shutting Down')
                    return None

                if choice == '':
                    choice = 0

                choice = int(choice)
                view_model.choice_list[choice]
                return choice

            except ValueError:

                print 'Sorry, %s not valid. Please Press ENTER or valid number' % choice

                choice = raw_input()

            except IndexError:

                print 'Sorry, There is no Option %s' % choice

                choice = raw_input()

    def border(self, ga_frame, pl_frame, an_frame, uv_frame, db=None):
        border_char = db.BorderChar

        def seperator():
            sep = border_char * (self.map_len + 2)
            sep += '\n'

            return sep

        final_string = seperator()

        while len(ga_frame) < self.map_len:
            ga_frame += ' '

        final_string += border_char + ga_frame + border_char + '\n'

        final_string += seperator()

        spl_player_frame = pl_frame.split('\n')
        for line in spl_player_frame:
            line_string = border_char + line

            while len(line_string) <= self.map_len:
                line_string += ' '

            line_string += border_char + '\n'

            final_string += line_string

        final_string += seperator()

        while len(an_frame) < self.map_len:
            an_frame += ' '

        final_string += border_char + an_frame + border_char + '\n'

        final_string += seperator()

        spl_uv_frame = uv_frame.split('\n')
        for line in spl_uv_frame:
            final_string += border_char + line + border_char + '\n'

        final_string += seperator()

        return final_string

    def drawMap(self, startConfig):
        maxCoordinates = startConfig.MaxCoordinates
        minCoordinates = startConfig.MinCoordinates

        universeExpansion_x = maxCoordinates[0] - minCoordinates[0]
        universeExpansion_y = maxCoordinates[1] - minCoordinates[1]

        # VizUniverse Map
        universeMatrix = list()

        # Problems with negative Coordinates
        # Currently 2-Dims Only
        for verticalSlice in range(universeExpansion_y):
            # Vertical Slices through Space
            verticalSlice = list()

            for point_in_space in range(universeExpansion_x):
                point_in_space = [self.view_db.MapIdentifiers['Empty'], self.view_db.MapIdentifiers['Empty']]

                verticalSlice.append(point_in_space)

            universeMatrix.append(verticalSlice)

        return universeMatrix

    def window_inserter(self, window_list, position_list):

        for i, window in enumerate(window_list):
            log.info('Get Position')
            position = position_list[i]

            log.info('Convert String to Matrix')
            matrix = self.string2matrix(window)

            log.info('Calc Window Position')
            x_rng, y_rng = self.calculate_window_range(matrix, position)

            log.info('Insert Window')
            self.insert_window(matrix, [x_rng, y_rng])


    def calculate_window_range(self, matrix, position):

        log.info('Needed Rows: %s, Needed Points: %s' % (len(matrix), len(matrix[0])))

        log.info('Starting Coordinates %s' % position)
        anm_y = position[1]
        anm_x = position[0]

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

                log.info('Overwriting %s with %s [%s]' % (
                                    self.uvMatrix[map_y][map_x][0], point_one, [map_x, map_y])
                                    )

                try:
                    point_two = matrix[matrix_y][matrix_x][1]
                     
                except IndexError:
                    point_two = ' ' * self.point_len

                log.info('Overwriting %s with %s' % (self.uvMatrix[map_y][map_x][1], point_two))

                self.uvMatrix[map_y][map_x] = [point_one, point_two]

                matrix_x += 1

            matrix_y += 1


    def string2matrix(self, rawString):
        row_splitted = rawString.split('\n')
        log.info('Splitted String to %s' % row_splitted)

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

            log.debug('Make same length: %s, %s' % (row_one, row_two))
            while len(row_one) < len(row_two):
                row_one.append(' ' * self.point_len)

            while len(row_two) < len(row_one):
                row_two.append(' ' * self.point_len)

            log.info('Zipping: %s, %s' % (row_one, row_two))
            for i, unn in enumerate(row_one):

                row.append([row_one[i], row_two[i]])

            row_one_counter += 2
            row_two_counter += 2

            matrix.append(row)

        log.info('Matrix Generated: %s' % matrix)
        return matrix


