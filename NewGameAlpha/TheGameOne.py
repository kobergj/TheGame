import setup as h
import interfaces as p
import sys

if __name__ == '__main__':
    terminal = h.SetUp(sys.argv)

    player = p.PlayerInterface('My Name')

    while player:
        nextaction = terminal(player)

        player(nextaction)
