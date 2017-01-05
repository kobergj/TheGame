import multiprocessing

import logging
import viewmodels.universe_vm as uvm


log = logging.getLogger('viewmodel')

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
        # self.killProducer()
        self.producingThread.join()

    def killProducer(self):
        # Sad it is...
        self.dead = True

    def __call__(self):
        log.info('Getting Models')
        universe, player = self.model_conn.recv()

        log.info('Start ViewModel Producing')
        # Start at Universe. Configurabe?
        view_model = uvm.UniverseViewModel(universe, player, False)

        while True:
            log.info('Sending View Model')
            self.view_conn.send(view_model)

            log.info('Awaiting Player Choice')
            players_choice = self.view_conn.recv()

            if players_choice is None:
                self.model_conn.send(None)
                break

            log.info('Execute %s' % view_model)
            view_model_class, change_func = view_model(players_choice)

            log.info('Sending %s' % change_func)
            self.model_conn.send(change_func)

            log.info('Getting New Models')
            universe, player = self.model_conn.recv()

            log.info('Initialize View Model %s' % view_model_class)
            view_model = view_model_class(universe, player, view_model.parent)

        log.info('View Model Producer dead and gone')








