from models.constants import RelativePositions as rp

import helpers.logger as log
import images as i


class View:
    def __init__(self, imgpathes):
        self._imgsrc = i.ImageSource(imgpathes)

    def __call__(self, gamemodel, controller):
        # Buy Action
        self.RegisterInteraction(gamemodel.Buy(), controller, rp.BottomRight)
        # Sell Action
        self.RegisterInteraction(gamemodel.Sell(), controller, rp.BottomLeft)
        # Player Stats
        self.RegisterInteraction(gamemodel.Stats(), controller, rp.TopLeft)
        # Travel Action
        self.RegisterInteraction(gamemodel.Travel(), controller, rp.TopRight)
        # Main Info
        self.RegisterInteraction(gamemodel.Harbor(), controller, rp.Center)

    @log.Logger('RegisterInteraction')
    def RegisterInteraction(self, interaction, controller, position):
        func = interaction.Func()
        validator = interaction.Validator()
        imgstry = self._imgsrc.ParentStrategy(interaction.Type())
        parent = controller.CheckSprite(position, imgstry, func=func, validator=validator)
        for args in interaction.Args():
            imgstry = self._imgsrc.ChildStrategy(interaction.Type(), args)
            controller.CheckSprite(position, imgstry, parent=parent, args=args)
