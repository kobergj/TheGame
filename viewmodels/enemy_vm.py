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


import consuming.visualization.universe as vui


def flushTerminal():
    print '\n' * 100


def showFightInfo(Ship, Enemy):
    longInfo = """
        You:    Attack Power: ATTACK    Defense: CURRENTHP/MAXHP
                            -- vs --
        Enemy:  Attack Power: EMATK     Defense: EMCDEF/EMMAXDEF

            [ENTER] Fight!      [1] Flee..
    """
    

    longInfo = longInfo.replace('ATTACK', str(Ship.attackPower()))
    longInfo = longInfo.replace('CURRENTHP',str(Ship.shieldStrength()))
    longInfo = longInfo.replace('MAXHP', str(Ship.shieldStrength.startValue))

    longInfo = longInfo.replace('EMATK', str(Enemy.attackPower()))
    longInfo = longInfo.replace('EMCDEF', str(Enemy.shieldStrength()))
    longInfo = longInfo.replace('EMMAXDEF', str(Enemy.shieldStrength.startValue))

    print longInfo

    choice = raw_input()

    while choice not in ['', '1']:
        choice = vui.invalidChoice(choice)

    if choice == '':
        return True


def endOfRound(Ship, Enemy, PlayersDice, EnemiesDice):
    players_atk = Ship.attackPower() + PlayersDice
    enemies_atk = Enemy.attackPower() + EnemiesDice

    flushTerminal()

    print '--' * 40

    longInfo = """
        You threw a PLAYERSDICE -- Enemy threw a ENEMIESDICE

        You PLAYERATK - ENEMYATK Enemy

        LOOSERTAKES DAMAGE Damage Points
    """

    longInfo = longInfo.replace('PLAYERSDICE', str(PlayersDice))

    longInfo = longInfo.replace('ENEMIESDICE', str(EnemiesDice))

    longInfo = longInfo.replace('PLAYERATK', str(players_atk))

    longInfo = longInfo.replace('ENEMYATK', str(enemies_atk))

    damage = players_atk - enemies_atk

    if damage >= 0:
        looser = 'Enemy takes'
    else:
        looser = 'You take'

    longInfo = longInfo.replace('LOOSERTAKES', str(looser))

    longInfo = longInfo.replace('DAMAGE', str(abs(damage)))

    print longInfo

    print '--' * 40


def fightWon(Ship, Enemy):
    fightWonInfo = """
        Congratz. Fight Won.

        Rewards:
            Credits: CREDITAMOUNT
            Goods: GOODS

        Press Enter to Continue
    """
    fightWonInfo = fightWonInfo.replace('CREDITAMOUNT', str(Enemy.lootableCredits))

    fightWonInfo = fightWonInfo.replace('GOODS', str(Enemy.inCargo))

    print fightWonInfo

    raw_input()


def fightLost():
    print 'Your Enemy was stronger'
    print 'Game Over'
