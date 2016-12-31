import logger as h


class Terminal:
    def __init__(self, config=None):
        self.choicemessage = 'Make Your Choice  -->  '

    @h.Logger('Call Terminal')
    def __call__(self, player):
        controller = TerminalController(self.choicemessage)

        harbor = player.CurrentHarbor()

        choices = player.Choices()

        with TerminalView(choices, harbor) as view:
            choice = controller(choices)
            view(choice)

        return choice


class TerminalView:
    def __init__(self, choices, harbor):
        self.choices = choices

        self.harborname = harbor.name

    def __enter__(self):
        # Build Things Up
        print 'You are at ' + self.harborname + '\n'
        i = 0
        for choice in self.choices:
            print i, str(choice)
            i += 1

        return self

    def __call__(self, choice):
        print 'You Have Choosen ' + str(choice)

    def __exit__(self, type, value, tb):
        # Tear things down
        print '\n'
        print ' ----- ----- ----- ------'
        print '\n'


class TerminalController:
    def __init__(self, inputmessage):
        self.inputmessage = inputmessage

    @h.Logger('Call Terminal Controller')
    def __call__(self, choicelist):
        numberofchoices = len(choicelist)

        choice = -1
        while int(choice) not in range(numberofchoices):
            choice = raw_input(self.inputmessage)

        return choicelist[int(choice)]
