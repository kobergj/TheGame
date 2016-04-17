import view.basic_view as bv

class UniverseView(bv.View):

    def __init__(self, Universe, Player, act_anmy):

        bv.View.__init__(self, Universe, Player)

        self.detail_window = self.travel_details(act_anmy)

        self.window_position = act_anmy.coordinates

        self.anomalyInfoLine = self.anomaly_info(act_anmy)

        self.choiceList = [True, False]

    def travel_details(self, anomaly):

        details = self.mapIdentifiers['Highlight'][0]

        details += '\n'

        details += self.mapIdentifiers['Highlight'][1] % anomaly.travelCosts

        return details


class AnomalyView(bv.View):

    def __init__(self, Universe, Player, avail_secs):

        bv.View.__init__(self, Universe, Player)

        self.detail_window = self.anomaly_details(avail_secs)

        self.choiceList = avail_secs

    def anomaly_details(self, availableSections):
        sectionInfo = 'Welcome to %s %s\n' % (self.act_anmy.__class__.__name__, self.act_anmy.name)
        for i, section in enumerate(availableSections):
            sectionInfo += " [%s] %s\n" % (i, section.infoString())

        return sectionInfo

class SectionView(bv.View):

    def __init__(self, Universe, Player, active_sec):
        bv.View.__init__(self, Universe, Player)

        self.detail_window = self.section_details(active_sec)

        self.choiceList = [None]

        for item in active_sec:
            self.choiceList.append(item)

    def section_details(self, Section):
        # Build Information
        interactionInfo = ''

        interactionInfo += "%s %s" % (self.act_anmy.__class__.__name__, self.act_anmy.name)

        interactionInfo += " -- %s\n"  % Section.infoString()

        interactionInfo += " [0] Back\n"

        for i, item in enumerate(Section):
            interactionInfo += " [%s] %s for %s\n" % (i+1, item.name, item.price)

        return interactionInfo
