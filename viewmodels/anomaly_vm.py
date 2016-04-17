# import logbook.configuration as log

import viewmodels.section_vm as svm

class AnomalyViewModel:

    def __init__(self, Anomaly, Player):
        """Checks for possible Actions with Anomaly"""
        sectionList = [svm.Spaceport, svm.Merchant, svm.Trader, svm.EquipmentDealer, svm.Gateport, svm.Quit]

        availableSections = list()

        for possibleSection in sectionList:

            try:
                section = possibleSection(Anomaly, Player)

                availableSections.append(section)

            except AttributeError:
                pass

        self.sections = availableSections

    def __iter__(self):
        return iter(self.sections)

