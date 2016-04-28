import multiprocessing

import configuration.log_details as log
import viewmodels.universe_vm as uvm

class ViewModelProducer:

    def __init__(self, universe, player, queue):

        self.producingThread = multiprocessing.Process(
            name='ViewModelProducer',
            target=self.producingFunction,
            args=(universe, player)
            )

        # Set Kill Switch
        self.dead = False

        # Assign Queue
        self.queue = queue

    def startProducing(self):
        # Start Thread
        self.producingThread.start()

    def stopProducing(self):
        # Stop Process
        self.producingThread.start()

    def killProducer(self):
        # Sad it is...
        self.dead = True

    def producingFunction(self, universe, player):
        # Start at Universe. Configurabe?
        view_model = uvm.UniverseViewModel(universe, player, False)

        while not self.dead:
            # Put it In
            self.queue.put(view_model)
            log.log('Awaiting Player Choice')
            players_choice = self.queue.get()

            log.log('Execute %s' % view_model)
            view_model_class = view_model(players_choice)

            log.log('Initialize View Model %s' % view_model_class)
            view_model = view_model_class(universe, player, view_model.parent)








