
import helpers.logger as log
import images as i


class View:
    def __init__(self, imgpathes):
        self._imgsrc = i.ImageSource(imgpathes)

    def __call__(self, gamemodel, controller):
        # Buy Action
        self.RegisterInteraction(gamemodel.Buy(), controller.SetBottomRight)
        # Sell Action
        self.RegisterInteraction(gamemodel.Sell(), controller.SetBottomLeft)
        # Player Stats
        self.RegisterInteraction(gamemodel.Stats(), controller.SetTopLeft)
        # Travel Action
        self.RegisterInteraction(gamemodel.Travel(), controller.SetTopRight)
        # Main Info
        self.RegisterInteraction(gamemodel.Harbor(), controller.SetCenter)

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
