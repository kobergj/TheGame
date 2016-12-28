import choices as act


class Player:
    def __init__(self, name, startharbor):
        self.name = name

        self._harbor = startharbor

        self._ingamingmood = True

    def __call__(self, action):
        if str(action) == 'Fly Away':
            self._ingamingmood = False

        action(self)

    def __nonzero__(self):
        return self._ingamingmood

    def Choices(self):
        harbor = self._harbor

        return [
            act.Action('Buy Item', harbor),
            act.Action('Sell Item', harbor),
            act.Action('Fly Away', harbor),
        ]

    def CurrentHarbor(self):
        return self._harbor
