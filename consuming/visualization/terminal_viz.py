import logbook.configuration as log

class MainScreen():
    # Where to store them best? 7   ' A12D12'
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
                      'Highlight':  ' ->XX<-'
                      }

    def __init__(self, Universe, Player):
        self.uvMatrix = self.drawMap(Universe, Player)

    def __call__(self, furtherInfo=None):

        self.showUniverse(furtherInfo)

        raw_input()

    def showAnomaly(self, Anomaly, Player):
        sample_info = [
          [
            ['    -->', 'Your Ad'],
            ['<--    ', 'd Here!'],
            ['ThirdTe', '       '],
            ['st --  ', '       ']
          ],[
            ['ThisIsA', '-------'],
            ['notherT', 'youKnew'],
            ['       ', '       '],
            ['       ', '       ']
          ]
        ]

        # Technical Approach
        anm_x = Anomaly.coordinates[:][0]
        anm_y = Anomaly.coordinates[:][1]

        needed_rows = len(sample_info)

        start_row = anm_y - needed_rows/2

        while start_row < 0:
            anm_y += 1
            start_row = anm_y - needed_rows/2

        end_row = start_row + len(sample_info)

        while end_row >= len(self.uvMatrix):
            anm_y -= 1
            start_row = anm_y - needed_rows/2
            end_row = start_row + len(sample_info)

        needed_points = len(sample_info[0])

        start_point = anm_x - needed_points/2

        while start_point < 0:
            anm_x += 1
            start_point = anm_x - needed_points/2

        end_point = start_point + len(sample_info[0])

        while end_point >= len(self.uvMatrix[0]):
            anm_x -= 1
            start_point = anm_x - needed_points/2
            end_point = start_point + len(sample_info[0])

        for i, j in enumerate(range(start_row, end_row)):

            for m, n in enumerate(range(start_point, end_point)):
                self.uvMatrix[j][n] = sample_info[i][m]

        self.showUniverse()

    def generateInteractionList(self, actList):
        i = 0

        while i < len(actList):
            first_line = actList[i]


            i += 1

            second_line = actList[i]




    def showUniverse(self, active=[-1,-1]):
        """Prints Universe Map. Highlights an Anomaly if given."""

        universeString = ''

        for y, row in enumerate(self.uvMatrix):
            first_line = ''
            second_line = ''

            for x, point in enumerate(row):
                first = point[0]

                if active == [x, y]:
                    first = self.highlight_line(first_line)

                first_line += first
                second_line += point[1]

            universeString += first_line + '\n' + second_line + '\n'

        print universeString

    def highlight_line(self, line):
        highlighted_line = self.mapIdentifiers['Highlight']
        to_replace = filter(lambda x: x.isalpha(), highlighted_line)

        anomalyIdentifiers = filter(lambda x: x.isalpha(), line)

        highlighted_line = highlighted_line.replace(to_replace, anomalyIdentifiers)

        return highlighted_line


    def drawMap(self, Universe, Player):
        # VizUniverse Map
        universeMatrix = list()

        # Loop through vertical Slices of Universe
        log.log('drawing Map')

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


                    if Player.currentPosition == anomaly.coordinates:
                        log.log('Current %s' % str(anomaly.coordinates))
                        second_line = second_line.replace('__', 'XX')

                    while len(first_line) < 7:
                        first_line += ' '

                    while len(second_line) < 7:
                        second_line += ' '

                row.append([first_line, second_line])

            universeMatrix.append(row)

        return universeMatrix
