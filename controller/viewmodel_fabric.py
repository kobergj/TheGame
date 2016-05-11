import multiprocessing

import configuration.log_details as log
import viewmodels.universe_vm as uvm

class ViewModelProducer:

    def __init__(self, model_connection, view_connection):

        self.producingThread = multiprocessing.Process(
            name='ViewModelProducer',
            target=self.__call__,
            # args=()
            )

        # Set Kill Switch
        self.dead = False

        # Connections
        self.model_conn = model_connection
        self.view_conn = view_connection

    def startProducing(self):
        # Start Thread
        self.producingThread.start()

    def stopProducing(self):
        # Stop Process
        self.killProducer()
        self.producingThread.join()

    def killProducer(self):
        # Sad it is...
        self.dead = True

    def __call__(self):
        log.log('Getting Models')
        universe, player = self.model_conn.recv()

        log.log('Start ViewModel Producing')
        # Start at Universe. Configurabe?
        view_model = uvm.UniverseViewModel(universe, player, False)

        while True:
            log.log('Sending View Model')
            self.view_conn.send(view_model)

            log.log('Awaiting Player Choice')
            players_choice = self.view_conn.recv()

            log.log('Execute %s' % view_model)
            view_model_class = view_model.next(players_choice)

            log.log('Sending Changes')
            self.model_conn.send(view_model)

            log.log('Getting New Models')
            universe, player = self.model_conn.recv()

            log.log('Initialize View Model %s' % view_model_class)
            view_model = view_model_class(universe, player, view_model.parent)

        log.log('View Model Producer dead and gone')








