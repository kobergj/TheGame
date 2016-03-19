import consuming.visualization.universe as vui


def flushTerminal():
    print '\n' * 100


def showFightInfo(Ship, Enemy):
    longInfo = """
        You:    Attack Power: ATTACK    Defense: CURRENTHP/MAXHP
                            -- vs --
        Enemy:  Attack Power: EMATK     Defense: EMCDEF/EMMAXDEF
    """
    

    longInfo = longInfo.replace('ATTACK', str(Ship.attackPower()))
    longInfo = longInfo.replace('CURRENTHP',str(Ship.shieldStrength()))
    longInfo = longInfo.replace('MAXHP', str(Ship.shieldStrength.startValue))

    longInfo = longInfo.replace('EMATK', str(Enemy.attackPower()))
    longInfo = longInfo.replace('EMCDEF', str(Enemy.shieldStrength()))
    longInfo = longInfo.replace('EMMAXDEF', str(Enemy.shieldStrength.startValue))

    print longInfo

    to_print = '\n' * 2
    to_print += '[ENTER] Fight!'

    to_print += '\n'
    to_print += '[1] Flee...'

    print to_print

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
