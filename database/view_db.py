

class TerminalView:
    MapIdentifiers = {'Empty':      '           ',
                      'Unknown':[   '           ',
                                    '     ?     ',
                                ],
                      'Planet':[    '    /Pl\   ',
                                    '    \__/   ',
                                ],    
                      'Spacegate':[ '     SG    ',
                                    '    /__\   ',
                                ],      
                      'Starbase':[  '    |SB|   ',
                                    '    |__|   ',
                                ],    
                      'Highlight':[ '   ->  <-   ',
                                    '   Travel   '
                                ],    
                      'Current': [  '   You are  ',
                                    '    Here    '
                                ],   
                      'CurHigh': [  '    Land    ',
                                    '    Here    '
                                ]
                      }

    GameInfoString = ' TheGame(Working Title) v0.6 '

    PlayerStatsTemplate =\
"""    Current Stats:
    Credits: %(credits)s    Reachable Planets: %(maxTravelDistance)s  Maintenance Costs: %(maintCosts)s
    Attack:  %(attackPower)s    Defense: %(curDef)s/%(maxDef)s  

    Cargo Bay: %(currentCargo)s/%(maxCargo)s -> %(inCargo)s
    Rooms:  %(currentRooms)s/%(maxRooms)s -> %(roomList)s"""

    BorderChar = '#'


    # Anomaly Info View not yet configurable

    # Anomaly View not yet configurable

    # Section View not yet configurable