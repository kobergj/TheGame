import logging

log = logging.getLogger('view')

def mainframe_view(Matrix, db=None):
    """Returns Universe Map as String."""
    universeString = ''

    for y, row in enumerate(Matrix):
        first_line = ''
        second_line = ''

        for x, point in enumerate(row):

            log.debug('Drawing %s' % point)
            first_line += point[0]
            second_line += point[1]

        universeString += first_line + '\n' + second_line + '\n'

    universeString = universeString[:-1]

    return universeString


def get_view(view_model, db=None):
    try:
        view_model.anomaly_availability
        uv_windows, uv_positions = universe_view(view_model, db.MapIdentifiers)
        return uv_windows, uv_positions
    except AttributeError:
        pass

    try:
        view_model.interactionType
        section_window = section_view(view_model)
        return [section_window], [view_model.anomaly.coordinates]
    except AttributeError:
        pass

    try:
        view_model.earned_goods
        victory_window = victory_view(view_model, db)
        return [victory_window], [view_model.anomaly.coordinates]
    except AttributeError:
        pass

    try:
        view_model.enemy
        fight_window = fight_view(view_model, db)
        return [fight_window], [view_model.anomaly.coordinates]
    except AttributeError:
        pass

    anomaly_window = anomaly_view(view_model)
    return [anomaly_window], [view_model.anomaly.coordinates]


def universe_view(view_model, mapIdentifiers):
    windows = list()
    positions = list()

    available_anomalies = view_model.anomaly_availability[0]

    for anomaly in available_anomalies:
        win = mapIdentifiers[anomaly.anomalytype]
        pos = anomaly.coordinates

        if anomaly.coordinates == view_model.anomaly.coordinates:
            win = mapIdentifiers['Highlight']

        if anomaly.coordinates == view_model.player.currentPosition:
            win = mapIdentifiers['Current']

            if anomaly == view_model.anomaly:
                win = mapIdentifiers['CurHigh']

        win = win[0] + '\n' + win[1]

        windows.append(win)
        positions.append(pos)

    not_available_anomalies = view_model.anomaly_availability[1]

    for anomaly in not_available_anomalies:
        win = mapIdentifiers['Unknown']
        pos = anomaly.coordinates

        win = win[0] + '\n' + win[1]

        windows.append(win)
        positions.append(pos)

    return windows, positions

def anomaly_view(view_model):
    sectionInfo = 'Welcome to %s %s\n' % (view_model.anomaly.__class__.__name__, view_model.anomaly.name)

    log.info('Pick Anomaly Section from %s' % view_model.choice_list)
    for i, section in enumerate(view_model.choice_list):

        if i == 0:
            sectionInfo += '[ENTER] Back\n'
            continue

        sectionInfo += " [%s] %s\n" % (i, section.__name__)

    return sectionInfo

def section_view(view_model):
    # Build Information
    interactionInfo = ''
    interactionInfo += "%s %s" % (view_model.anomaly.anomalytype, view_model.anomaly.name)
    interactionInfo += " -- %s\n"  % view_model.__class__.__name__

    log.info('Generating Sections string for %s' % map(str, view_model.choice_list))
    for i, item in enumerate(view_model.choice_list):
        if i == 0:
            interactionInfo += " [0] Back\n"
            continue

        # x = 'Buy'
        # if item in view_model.choice_list[:i]:
        #     x = 'Sell'

        interactionInfo += " [%s] %s %s for %s\n" % (i, view_model.interactionType, item.name, item.price)

    return interactionInfo

def fight_view(view_model, db):

    fight_info = {
        'pl_curDef': view_model.player.currentShip.shieldStrength(),
        'pl_maxDef': view_model.player.currentShip.shieldStrength.startValue,
        'pl_atk':    view_model.player.currentShip.attackPower(),

        'em_curDef': view_model.enemy.shieldStrength(),
        'em_maxDef': view_model.enemy.shieldStrength.startValue,
        'em_atk':    view_model.enemy.attackPower(),
    }

    return db.FightTemplate % fight_info


def victory_view(view_model, db):

    victory_info = {
        'credits': view_model.earned_creds,
        'goods': map(str, view_model.earned_goods)
    }

    return db.VictoryTemplate % victory_info
