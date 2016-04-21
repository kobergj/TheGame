# import logbook.configuration as log

import viewmodels.basic_vm as bvm
import viewmodels.section_vm as svm

class AnomalyViewModel(bvm.BasicViewModel):

    def __init__(self, Universe, Player, UniverseViewModel):
        """Checks for possible Actions with Anomaly"""
        Anomaly = Universe[Player.currentPosition]

        bvm.BasicViewModel.__init__(self, Anomaly, Player)

        section_vm_list = [
            svm.Merchant  #, svm.Trader, svm.EquipmentDealer, svm.Gateport, svm.Quit
            ]

        availableViewModels = [UniverseViewModel]

        for possibleSection in section_vm_list:

            try:
                possibleSection(Universe, Player, AnomalyViewModel)

                availableViewModels.append(possibleSection)

            except AttributeError:
                pass

        self.choice_list = availableViewModels

        self.parent = UniverseViewModel

    def __iter__(self):
        return iter(self.sections)

    def __call__(self):
        return self.choice_list[self.player_choice]

