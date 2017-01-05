

class TerminalView:
    MapIdentifiers = {'Empty': [    '           ',
                                    '           '
                                ],
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

    FightTemplate =\
"""     FIGHT
    You:    Enemy:
    %(pl_curDef)s/%(pl_maxDef)s     %(em_curDef)s/%(em_maxDef)s
    %(pl_atk)s      %(em_atk)s
    [ENTER] Attack   --   [1] Flee
"""

    VictoryTemplate =\
""" Congrats. You won. Earned Credits: %(credits)s, Earned Goods: %(goods)s"""

    InfoFrameTemplate =\
"""     [ENTER] %(emyAmount) """



    # Anomaly Info View not yet configurable

    # Anomaly View not yet configurable

    # Section View not yet configurable