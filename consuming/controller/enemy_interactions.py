import consuming.visualization.fights as viz

import random


def beginFight(Ship, Enemy):
    viz.flushTerminal()

    # Fight or Flee
    fight = viz.showFightInfo(Ship, Enemy)

    while fight:
        # Players Dice
        players_dice = random.randint(1, 6)
        # Enemies Dice
        enemies_dice = random.randint(1, 6)
        # Players Atk
        players_atk = Ship.attackPower() + players_dice
        # Enemies Atk
        enemies_atk = Enemy.attackPower() + enemies_dice
        # Damage
        damage = abs(players_atk - enemies_atk)

        if players_atk > enemies_atk:
            # Player won round
            Enemy.shieldStrength.addBoost(damage*-1)

        elif enemies_atk > players_atk:
            # Enemy wins round
            Ship.shieldStrength.addBoost(damage*-1)

        fight = viz.endOfRound(Ship, Enemy, players_dice, enemies_dice)

        if Ship.shieldStrength() <= 0:
            viz.fightLost()

            quit()

        if Enemy.shieldStrength() <= 0:
            viz.fightWon(Ship, Enemy)

            return True

        # Fight or Flee
        fight = viz.showFightInfo(Ship, Enemy)
