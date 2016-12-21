# import logbook.configuration as log
import logging

import viewmodels.basic_vm as bvm
import viewmodels.section_vm as svm

import controller.model_operations as mo

log = logging.getLogger('viewmodel')

class AnomalyViewModel(bvm.BasicViewModel):

    def __init__(self, Universe, Player, UniverseViewModel):
        """Checks for possible Actions with Anomaly"""
        Anomaly = Universe[Player.currentPosition]

        bvm.BasicViewModel.__init__(self, Anomaly, Player, UniverseViewModel)

        section_vm_list = [
            svm.Merchant, svm.Trader, svm.EquipmentDealer, svm.Gateport
            ]

        availableViewModels = [UniverseViewModel]

        for possibleSection in section_vm_list:

            try:
                possibleSection(Universe, Player, AnomalyViewModel)

                availableViewModels.append(possibleSection)

            except AttributeError as e:
                log.info('%s not available: %s' % (possibleSection, e))
                pass

        self.choice_list = availableViewModels

    def __iter__(self):
        return iter(self.sections)

    def __call__(self, player_choice):
        self.player_choice = player_choice

        next_view_model = self.choice_list[player_choice]

        return next_view_model, mo.Pass()

