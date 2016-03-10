import consuming.visualization.universe as vui


def flushTerminal():
    print '\n' * 100


def showFightInfo(Ship, Enemy):
    to_print = ''

    to_print += 'You: Atk:%s HP:%s' % (str(Ship.attackPower), str(Ship.shieldStrength))
    to_print += '\nvs.\n'
    to_print += 'Enemy: Atk:%s HP:%s' % (str(Enemy.attackPower), str(Enemy.shieldStrength))

    to_print += '\n'*2
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
    print '--' * 20

    to_print = ''

    to_print += 'You threw a %s' % PlayersDice

    to_print += '\n'

    to_print += 'Enemy threw a %s' % EnemiesDice

    to_print += '\n'

    players_atk = Ship.attackPower + PlayersDice
    enemies_atk = Enemy.attackPower + EnemiesDice

    damage = players_atk - enemies_atk

    if damage > 0:
        to_print += 'You win '
    else:
        to_print += 'You loose '

    to_print += '%s:%s' % (str(players_atk), str(enemies_atk))

    to_print += '\n'

    if damage > 0:
        to_print += 'Enemy looses '
    else:
        to_print += 'You loose '

    to_print += '%s Hit Points' % str(abs(damage))

    print to_print

    print '--' * 20


def fightWon():
    print 'Congratz. Fight Won.'
    print 'Press Enter to Continue'

    raw_input()


def fightLost():
    print 'Your Enemy was stronger'
    print 'Game Over'
