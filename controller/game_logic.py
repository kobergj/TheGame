
import configuration.database as db
import configuration.log_details as log

import controller.model_fabric as mf

import viewmodels.universe_vm as uvm
import viewmodels.anomaly_vm as avm
import viewmodels.anomaly_vm as svm

class RandomGame:

    def __init__(self, pl_info, uv_size, sh_stats, an_num):

    def __call__(self, old_view_model):

        view_models = [uvm.Universe, avm.Anomaly, svm.Section]

        i = view_models.index(old_view_model.__class__)

        view_model = old_view_model()

        if not view_model:
            view_model = view_models[i-1](self.universe, self.player)

        return view_model


    def fillUniverse(self, NumberOfAnomalies):

        for i in range(NumberOfAnomalies):
            # Get Anomaly
            anomaly = mf.produceAnomaly(self.database)
            # Add Anomaly
            self.universe.addAnomaly(anomaly)
