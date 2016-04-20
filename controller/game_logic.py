
import configuration.database as db
import configuration.log_details as log

import controller.model_fabric as mf

import viewmodels.universe_vm as uvm
import viewmodels.anomaly_vm as avm
import viewmodels.anomaly_vm as svm

class RandomGame:

    def __init__(self, pl_info, uv_size, sh_stats, an_num):
        log.log('Init Database')
        self.database = db.DynamicDatabase[:]

        log.log('Assigning Player')
        self.player = mf.producePlayer(pl_info)

        log.log('Generate Universe')
        self.universe = mf.produceUniverse(uv_size)

        log.log('Initialize Producer')
        self.randomProducer = mf.randomProducer(self.database, self.universe)

        log.log('Craft Ship')
        startingShip = mf.produceShip(self.database, sh_stats)

        log.log('Board Ship')
        self.player.switchShip(startingShip)


        log.log('Set Starting Anomaly')
        startingAnomaly = mf.produceAnomaly(self.database)
        self.universe.addAnomaly(startingAnomaly)
        self.player.travelTo(startingAnomaly.coordinates)

        log.log('Fill Universe')
        self.fillUniverse(self.universe, an_num)
        self.universe.update(self.player)

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
