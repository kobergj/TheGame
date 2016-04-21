import threading

import viewmodels.universe_vm as uvm

class ViewModelProducer:

    def __init__(self, universe, player, queue):

        self.producingThread = threading.Thread(
            name='ViewModelProducer',
            target=self.producingFunction,
            args=(universe, player)
            )

        # Make Her a Daemon
        # self.producingThread.daemon = True

        # Set Kill Switch
        self.dead = False

        self.queue = queue

    def startProducing(self):
        self.producingThread.start()

    def killProducer(self):
        self.dead = True

    def producingFunction(self, universe, player):

        view_model = uvm.UniverseViewModel(universe, player, False)

        while not self.dead:

            self.queue.put(view_model)

            while view_model.player_choice is None:
                pass

            view_model_class = view_model()

            view_model = view_model_class(universe, player, view_model.parent)








