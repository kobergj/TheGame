

class FleetViewer:
    def __init__(self, fleet):
        self._fleet = fleet

    def GetStat(self, statname):
        return self._fleet.stats[statname]
