from models.constants import InteractionTypes as it

import helpers.logger as log
import images as i


class View:
    def __init__(self, imgpathes, controller):
        self._imgsrc = i.ImageSource(imgpathes)

        self._layout = {
            it.Buy: controller.SetBottomRight,
            it.Sell: controller.SetBottomLeft,
            it.Stats: controller.SetTopLeft,
            it.Travel: controller.SetTopRight,
            it.Info: controller.SetCenter,
            it.GameOver: controller.SetCenter,
        }

    def __call__(self, gamemodel, controller):
        for interaction in gamemodel.Interactions():
            typ = interaction.Type()
            self.RegisterInteraction(interaction, self._layout[typ])

    @log.Logger('RegisterInteraction')
    def RegisterInteraction(self, interaction, ctrlregistry):
        # Generate ImageStrategy
        typ = interaction.Type()
        imgstry = self._imgsrc.ParentStrategy(typ)

        # Get/Set parent
        func = interaction.Func()
        validator = interaction.Validator()
        parent = ctrlregistry(imgstry, func=func, validator=validator)

        # Loop through Arguments
        for args in interaction.Args():
            # Generate ImageStrategy
            imgstry = self._imgsrc.ChildStrategy(typ, args)

            # Set Child
            ctrlregistry(imgstry, parent=parent, args=args)
