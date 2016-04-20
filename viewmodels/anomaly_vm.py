# import logbook.configuration as log

import viewmodels.basic_vm as bvm
import viewmodels.section_vm as svm

class AnomalyViewModel(bvm.BasicViewModel):

    def __init__(self, Anomaly, Player, UniverseViewModel):
        """Checks for possible Actions with Anomaly"""
        bvm.BasicViewModel.__init__(self, Anomaly, Player)

        section_vm_list = [
            svm.Merchant, svm.Trader, svm.EquipmentDealer, svm.Gateport, svm.Quit
            ]

        availableViewModels = [UniverseViewModel]

        for possibleSection in section_vm_list:

            try:
                section = possibleSection(Anomaly, Player, AnomalyViewModel)

                availableViewModels.append(section)

            except AttributeError:
                pass

        self.choiceList = availableViewModels

    def __iter__(self):
        return iter(self.sections)

    def __call__(self):
        return self.choiceList[self.player_choice]

