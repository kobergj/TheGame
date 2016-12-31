
class Action:
    def __init__(self, name, context):
        self.name = name
        self.context = context

    def __str__(self):
        return self.name

    def __call__(self, player):
        # Some Action here
        # For Ex
        return True

    def available(self, player):
        # Returns True if Action is available for player
        return True


# Action BuyItem
class BuyItem(Action):
    def __call__(self, player):
        item = self.context

        player.Credits(item.price)
        player.Cargo(item)

        return

    def available(self, player):
        item = self.context

        if player.Credits() >= item.price:
            return True

        return False


# Action Travel
class Travel(Action):
    def __call__(self, player):
        space = self.context

        destination = space.destination

        player._harbor = destination

        return True


# Action Quit
class Quit(Action):
    def __call__(self, player):
        player.ingamingmood = False
        return False
