import interfaces as i
import factory as f


class MainController:
    def __init__(self):
        playerfactory = f.PlayerFactory()
        self.playerInterface = i.PlayerInterface(playerfactory)

        spacefactory = f.SpaceFactory()
        self.spaceInterface = i.SpaceInterface(spacefactory)

        harborfactory = f.HarborFactory()
        self.harborInterface = i.HarborInterface(harborfactory)
