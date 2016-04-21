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
        view_model.available_anomalies
        uv_windows, uv_positions = universe_view(view_model, mapIdents)
        return uv_windows, uv_positions
    except AttributeError:
        pass

    try:
        view_model.parent
        section_window = section_view(view_model)
        return [section_window], view_model.anomaly.coordinates
    except AttributeError:
        pass

    anomaly_window = anomaly_view(view_model)
    return [anomaly_window], view_model.anomaly.coordinates


def universe_view(view_model, mapIdentifiers):
    windows = list()
    positions = list()

    for anomaly in view_model.available_anomalies:
        win = mapIdentifiers[anomaly.__class__.__name__]
        pos = anomaly.coordinates

        if anomaly == view_model.anomaly:
            win = mapIdentifiers['Highlight']

        if anomaly == view_model.player.currentPosition:
            win = mapIdentifiers['Current']

        win = win[0] + '\n' + win[1]

        windows.append(win)
        positions.append(pos)

    return windows, positions

def anomaly_view(view_model):
    sectionInfo = 'Welcome to %s %s\n' % (view_model.anomaly.__class__.__name__, view_model.anomaly.name)

    for i, section in enumerate(view_model.choice_list):

        sectionInfo += " [%s] %s\n" % (i, section.__class__.__name__)

    return sectionInfo

def section_view(view_model):
    # Build Information
    interactionInfo = ''
    interactionInfo += "%s %s" % (view_model.anomaly.__class__.__name__, view_model.anomaly.name)
    interactionInfo += " -- %s\n"  % view_model.__class__.__name__

    interactionInfo += " [0] Back\n"

    for i, item in enumerate(view_model.available_options):
        interactionInfo += " [%s] %s for %s\n" % (i+1, item.name, item.price)

    return interactionInfo
