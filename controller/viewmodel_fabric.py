import threading

import viewmodels.universe_vm as uvm
import viewmodels.anomaly_vm as avm
import viewmodels.anomaly_vm as svm


class ViewModelProducer:

    def __init__(self, universe, player, queue):

        self.producingThread = threading.Thread(
            name='ViewModelProducer',
            target=self.producingFunction,
            args=(universe, player)
            )

        # Make Her a Daemon
        self.producingThread.daemon = True

        # Set Kill Switch
        self.dead = False

        self.queue = queue

    def startProducing(self):
        self.producingThread.start()

    def killProducer(self):
        self.dead = True

    def producingFunction(self, universe, player):

        view_models = [uvm.Universe]

        self.queue.put(view_models[0])

        while not self.dead:

            while not self.queue.empty():
                pass

            view_model = self.queue.get()

            if not view_model:
                view_model = view_models.pop()

            view_model(universe, player)

            self.queue.put(view_model)






