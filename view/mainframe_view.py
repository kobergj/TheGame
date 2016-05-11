import configuration.log_details as log

def mainframe_view(Matrix):
    """Returns Universe Map as String."""
    universeString = ''

    for y, row in enumerate(Matrix):
        first_line = ''
        second_line = ''

        for x, point in enumerate(row):

            log.log('Drawing %s' % point, level=10)
            first_line += point[0]
            second_line += point[1]

        universeString += first_line + '\n' + second_line + '\n'

    return universeString


def get_view(view_model, mapIdents):
    try:
        view_model.anomaly_availability
        uv_windows, uv_positions = universe_view(view_model, mapIdents)
        return uv_windows, uv_positions
    except AttributeError:
        pass

    try:
        view_model.interactionType
        section_window = section_view(view_model)
        return [section_window], [view_model.anomaly.coordinates]
    except AttributeError:
        pass

    anomaly_window = anomaly_view(view_model)
    return [anomaly_window], [view_model.anomaly.coordinates]


def universe_view(view_model, mapIdentifiers):
    windows = list()
    positions = list()

    available_anomalies = view_model.anomaly_availability[0]

    for anomaly in available_anomalies:
        win = mapIdentifiers[anomaly.__class__.__name__]
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

    log.log('Pick Anomaly Section from %s' % view_model.choice_list)
    for i, section in enumerate(view_model.choice_list):

        if i == 0:
            sectionInfo += '[ENTER] Back\n'
            continue

        sectionInfo += " [%s] %s\n" % (i, section.__name__)

    return sectionInfo

def section_view(view_model):
    # Build Information
    interactionInfo = ''
    interactionInfo += "%s %s" % (view_model.anomaly.__class__.__name__, view_model.anomaly.name)
    interactionInfo += " -- %s\n"  % view_model.__class__.__name__

    log.log('Generating Sections string for %s' % view_model.choice_list)
    for i, item in enumerate(view_model.choice_list):
        if i == 0:
            interactionInfo += " [0] Back\n"
            continue

        interactionInfo += " [%s] %s for %s\n" % (i, item.name, item.price)

    return interactionInfo
