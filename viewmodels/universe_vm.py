import viewmodels.basic_vm as bvm

class UniverseViewModel(bvm.BasicViewModel):

    def __init__(self, universe, player):

        anomaly = universe[player.currentPosition]

        bvm.BasicViewModel.__init__(self, anomaly, player)

        
