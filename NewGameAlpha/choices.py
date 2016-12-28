
class Action:
    def __init__(self, name, harbor):
        self.name = name
        self.harbor = harbor

    def __str__(self):
        return self.name

    def __call__(self, player):
        # Some Action here
        # For Ex
        harbor = self.harbor

        return harbor
