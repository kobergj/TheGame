import logging

import gameinfo_view as gv
import infoframe_view as iv
import statframe_view as sv
import mainframe_view as mv

log = logging.getLogger('view')

class View:
    def __init__(self, database):
        self.view_db = database.TerminalView

        main_window_len = database.StartConfiguration.Universe.MaxCoordinates[1]
        main_window_height = database.StartConfiguration.Universe.MaxCoordinates[0]
        self.main_window = Window(database.TerminalView, [main_window_len, main_window_height])

        stat_window_len = main_window_len / 2
        stat_window_height = 3
        self.stat_window = Window(self.view_db, [stat_window_len, stat_window_height])

        self.window_len = main_window_len * self.main_window.point_len

    def __call__(self, view_model):
        log.info('Getting Windows Of %s' % view_model.__class__.__name__)
        windows, positions = mv.get_view(view_model, self.view_db)

        log.info('Inserting %s at %s' % (windows, positions))
        self.main_window.insert(windows, positions)
        self.stat_window.insert([sv.stat_view(view_model, db=self.view_db)], [[0, 0]])

        # Game Frame
        ga_view = gv.gameinfo_view(view_model, db=self.view_db)
        # Stat Frame
        pl_view = str(self.stat_window)
        # Anm Frame
        anm_view = iv.info_view(view_model.anomaly, db=self.view_db)
        # Universe Frame
        uv_view = str(self.main_window)

        log.info('Adding borders to %s' % [pl_view, anm_view, uv_view])
        complete_view = self.border(ga_view, pl_view, anm_view, uv_view, db=self.view_db)

        print '\n' * 100
        print complete_view

        choice = raw_input()
        log.info('Player choose %s' % choice)

        self.main_window.reset()

        while True:
            try:
                if choice == 'q':
                    log.info('Kill Flag. Shutting Down')
                    return None

                if choice == '':
                    log.info('Player pressed ENTER.')
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
            sep = border_char * (self.window_len + 2)
            sep += '\n'

            return sep

        final_string = seperator()

        while len(ga_frame) < self.window_len:
            ga_frame += ' '

        final_string += border_char + ga_frame + border_char + '\n'

        final_string += seperator()

        spl_player_frame = pl_frame.split('\n')
        for line in spl_player_frame:
            line_string = border_char + line

            while len(line_string) <= self.window_len:
                line_string += ' '

            line_string += border_char + '\n'

            final_string += line_string

        final_string += seperator()

        while len(an_frame) < self.window_len:
            an_frame += ' '

        final_string += border_char + an_frame + border_char + '\n'

        final_string += seperator()

        spl_uv_frame = uv_frame.split('\n')
        for line in spl_uv_frame:
            final_string += border_char + line + border_char + '\n'

        final_string += seperator()

        return final_string


class Window:
    def __init__(self, view_db, size):
        self.view_db = view_db

        rows = size[1]
        fields = size[0]

        self.matrix = self.initialize(rows, fields)
        # self._matrix = copy.deepcopy(self.uvMatrix)

        self.point_len = len(self.view_db.MapIdentifiers['Empty'][0])


    def initialize(self, rownumber, fieldnumber):
        # VizUniverse Map
        windowMatrix = list()

        # Currently 2-Dims Only
        for verticalSlice in range(rownumber):
            # Vertical Slices through Space
            verticalSlice = list()

            for point_in_space in range(fieldnumber):
                point_in_space = self.view_db.MapIdentifiers['Empty']

                verticalSlice.append(point_in_space)

            windowMatrix.append(verticalSlice)

        return windowMatrix

    def reset(self):
        self.matrix = self.initialize(len(self.matrix), len(self.matrix[0]))

    def insert(self, window_list, position_list):

        for i, window in enumerate(window_list):
            log.info('Get Position')
            position = position_list[i]

            log.info('Convert String to Matrix')
            matrix = self.string2matrix(window)

            log.info('Calc Window Position')
            x_rng, y_rng = self.calculate_window_range(matrix, position)

            log.info('Insert Window')
            self.insert_window(matrix, [x_rng, y_rng])


    def calculate_window_range(self, insertmatrix, position):

        log.info('Needed Rows: %s, Needed Points: %s' % (len(insertmatrix), len(insertmatrix[0])))

        log.info('Starting Coordinates %s' % position)
        anm_y = position[1]
        anm_x = position[0]

        # Should not happen
        while anm_y < 0:
            anm_y += 1

        # Calculate End Row Index
        end_row = anm_y + len(insertmatrix)

        # Fit in Map?
        while end_row > len(self.matrix):
            anm_y -= 1
            end_row = anm_y + len(insertmatrix)

        # Should not happen
        while anm_x < 0:
            anm_x += 1

        # Calculate End Point Index
        end_point = anm_x + len(insertmatrix[0])

        # Fit In Map?
        while end_point > len(self.matrix[0]):
            anm_x -= 1
            end_point = anm_x + len(insertmatrix[0])

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
                                    self.matrix[map_y][map_x][0], point_one, [map_x, map_y])
                                    )

                try:
                    point_two = matrix[matrix_y][matrix_x][1]
                     
                except IndexError:
                    point_two = ' ' * self.point_len

                log.info('Overwriting %s with %s' % (self.matrix[map_y][map_x][1], point_two))

                self.matrix[map_y][map_x] = [point_one, point_two]

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

    def __str__(self):
        """Returns Universe Map as String."""
        windowstring = ''

        for y, row in enumerate(self.matrix):
            first_line = ''
            second_line = ''

            for x, point in enumerate(row):

                log.debug('Drawing %s' % point)
                first_line += point[0]
                second_line += point[1]

            windowstring += first_line + '\n' + second_line + '\n'

        windowstring = windowstring[:-1]

        return windowstring

