


def info_view(Anomaly, db):
    # Needs to be made configurable
    if not Anomaly:
        return ' '

    # Possible Interaction
    amyname = Anomaly.name
    amytype = Anomaly.__class__.__name__

    information = '    [ENTER]  ' # % Anomaly.coordinates

    for enemy in Anomaly.orbit:
        information += 'X'

    information += ' %s %s ' % (amytype, amyname)

    information += ' Cost To Travel Here: %s '   # % Anomaly.travelCosts

    # Buys It Goods?
    try:
        buy_information = '- Buys '

        for good in Anomaly.goodsConsumed:
            buy_information += '%s@%s ' % (good.name, good.price)

        buy_information += ' '

        information += buy_information
    except AttributeError:
        pass

    # Sells it Goods?
    try:
        sell_information = '- Sells: '

        for good in Anomaly.goodsProduced:
            sell_information += '%s@%s ' % (good.name, good.price)

        sell_information += ' '

        information += sell_information

    except AttributeError:
        pass

    information += ' // [1] Next'

    return information
