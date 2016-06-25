
class BasicViewModel:

    def __init__(self, anomaly, player, parent_viewmodel):
        # Anomaly to Interact with
        self.anomaly = anomaly
        # Player
        self.player = player
        # Space for a choice
        self.player_choice = None
        # Available Choices - May be overwritten
        self.choice_list = [True, False]
        # Parent View Model
        self.parent = parent_viewmodel

        # Info Stats
        self.playerinfo = self.getplayerinfo(player)

    def __call__(self, universe, player):
        return self.parent

    def getplayerinfo(self, player):

        def cap(contentname):
            cnt = player.currentShip.access_content(contentname)
            return cnt.capacity()

        def maxcap(contentname):
            cnt = player.currentShip.access_content(contentname)
            return cnt.maxcapacity()

        return {
            'credits': player.credits,
            'attackPower': cap('weapon'),
            'curDef': cap('shield'),
            'maxDef': maxcap('shield'),
            'maxTravelDistance': cap('engine'),
            'maintCosts': None,
            'currentCargo': cap('cargobay'),
            'maxCargo': maxcap('cargobay'),
            'inCargo': player.currentShip.access_content('cargobay').asdict(),
            'currentRooms': 0,  #Player.currentShip.spaceForRooms.startValue - Player.currentShip.spaceForRooms(),
            'maxRooms': 0,  # Player.currentShip.spaceForRooms.startValue,
            'roomList': []
            }

