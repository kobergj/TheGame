
def Arrival(Anomaly, Player):
    # Flush Terminal
    print '\n' * 100

    # Border
    print '--' * 100

    information = generateInfoString(Anomaly, Player)

    print information

    # Border
    print '--' * 100

    options = generateOptionsString(Anomaly, Player)

    print options


def generateInfoString(Anomaly, Player):
    # Anomaly Type
    anomalyType = Anomaly.__class__.__name__
    # Init
    info = ''
    # Positonal Information
    info += "\n You are at %s %s" % (anomalyType, Anomaly.name)

    return info


def generateOptionsString(Anomaly, Player):
    # Init
    info = ''
    # Option Information
    for interaction in Anomaly.possibleActions:
        info += '\n[%s] %s' % (Anomaly.possibleActions.index(interaction), interaction)

    return info
