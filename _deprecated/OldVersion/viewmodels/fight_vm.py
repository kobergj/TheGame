import logging

import basic_vm as bvm

log = logging.getLogger('viewmodel')

class FightViewModel(bvm.BasicViewModel):

    def __init__(self, universe, player, UniverseViewModel):

        anomaly = universe[player.currentPosition]

        bvm.BasicViewModel.__init__(self, anomaly, player, UniverseViewModel)

        self.enemy = anomaly.enemies[0]

    def __call__(self, universe, player):
        anomaly = universe[player.currentPosition]
        enemy = anomaly.enemies[0]

        if self.flee_flag:
            # Enemy Gets repaired
            enemy.shieldStrength.reset()
            log.info('Player flew')
            return

        if enemy.shieldStrength <= 0:
            log.info('Player defeated Enemy %s' % enemy)
            credits = enemy.lootableCredits
            loot = enemy.lootableGoods

            log.info('Looted Credits: %s' % credits)
            player.earnCredits(credits)

            log.info('Looted Loot: %s' % loot)
            for good in loot:
                player.currentShip.loadCargo(good)

            log.info('Killing Enemy')
            anomaly.killEnemy()
            return

        if player.currentShip.shieldStrength() <= 0:
            log.info('Player defeated by Enemy %s' % enemy)
            player.dead = True
            return

        self.fight(player, enemy)
        return

    def fight(self, player, enemy):
        enemy.shieldStrength.addBoost(-900)


    def next(self, player_choice):

        self.flee_flag = player_choice

        if self.flee_flag:
            return self.parent

        if self.enemy.shieldStrength <= 0:
            log.info('Assigning Enemy %s to VicViewModel' % self.enemy)
            VictoryViewModel.enemy_wreck = self.enemy
            return VictoryViewModel

        return FightViewModel


class VictoryViewModel(bvm.BasicViewModel):

    def __init__(self, universe, player, UniverseViewModel):
        anomaly = universe[player.currentPosition]

        bvm.BasicViewModel.__init__(self, anomaly, player, UniverseViewModel)

        self.earned_creds = anomaly.dead_enemies[-1].lootableCredits
        self.earned_goods = anomaly.dead_enemies[-1].lootableGoods

        logging.info('Initialized VicViewModel: Creds:%s Loot:%s' % (self.earned_creds, self.earned_goods))

    def next(self, player_choice):
        if self.anomaly.enemies:
            return FightViewModel

        return self.parent






