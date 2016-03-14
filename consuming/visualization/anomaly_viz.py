
def chooseSection(Anomaly, Player, AvailableSections):
    # Flush Terminal
    print '\n' * 100

    # Border
    print '--' * 20

    # Information Screen
    information = generateInfoString(Anomaly, Player)
    print information

    # Border
    print '--' * 20

    # Option Screen
    options = generateSectionsString(AvailableSections)
    print options

    # Await Choice
    choice = input()

    # Not Valid Choice
    while choice not in range(len(AvailableSections)):
        print "Sorry %s not valid" % choice
        choice = input()

    return AvailableSections[choice]


def chooseInteraction(Anomaly, Player, Section):
    # Margin
    print '\n'*100
    # Border
    print '--' * 20
    # Gen Section Info
    secinfo = generateSectionInfoString(Section, Player)
    print secinfo
    # Gen Str
    interactions = generateInteractionsString(Section)
    print interactions
    # Await Choice
    choice = input()

    # Not Valid Choice
    while choice not in range(len(Section)+1):
        print "Sorry %s not valid" % choice
        choice = input()

    if choice == 0:
        return

    return Section[choice-1]


def generateInfoString(Anomaly, Player):
    # Anomaly Type
    anomalyType = Anomaly.__class__.__name__
    # Init
    info = ''
    # Positonal Information
    info += "\n You are at %s %s" % (anomalyType, Anomaly.name)

    return info


def generateSectionInfoString(Section, Player):
    secInfo = 'Current Stats: \n'

    for info in Section.correspondingStats:
        value = Section.correspondingStats[info]
        secInfo += " %s: %s \n" % (info, value)

    return secInfo


def generateSectionsString(PossibleActions):
    # Init
    info = ''
    # Option Information

    for interaction in PossibleActions:
        info += '\n[%s] %s' % (PossibleActions.index(interaction), interaction.infoString())

    return info


def generateInteractionsString(Section):
    # Gen Action String
    actStr = '[0] Back \n'
    # Loop
    for interaction, info in Section:
        actStr += '[' + str(Section.index(interaction)+1) + '] '
        actStr += Section.interactionType + ' ' + interaction
        actStr += ' for ' + str(info) + '\n'

    return actStr
