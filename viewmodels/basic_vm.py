
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

