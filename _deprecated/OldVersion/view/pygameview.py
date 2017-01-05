import pygame as pyg
import multiprocessing as mp


class PyGameView(mp.Process):
    def __init__(self, connection):
        mp.Process.__init__(self, name='pygameview')

        