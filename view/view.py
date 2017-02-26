from models.constants import RelativePositions as rp

import images as i


class View:
    def __init__(self, imgpathes):
        self._imgsrc = i.ImageSource(imgpathes)

    def __call__(self, gamemodel, controller):
        # Buy Action
        self.RegisterInteraction(gamemodel.Buy(), controller, rp.BottomRight)

    def RegisterInteraction(self, interaction, controller, position):
        func = interaction.Func()
        imgstry = self._imgsrc.ParentStrategy(interaction.Type())
        parent = controller.NewParentSprite(position, imgstry, func)
        for args in interaction.Args():
            imgstry = self._imgsrc.ChildStrategy(interaction.Type(), args)
            controller.NewChildSprite(position, imgstry, parent, args)
