import game_controller as gc
import harbor_models as hm
import terminal_view as tv

if __name__ == '__main__':
    player = gc.Player('My Name', hm.Harbor('Safe Harbor'))

    terminal = tv.Terminal()

    while player:
        nextaction = terminal(player)

        player(nextaction)
