import pygame
import logging
import time

BUTTONCOORDSONE = [0, 0]
TXTSONE = ['Please,\nClick me\nmy Friend!',
           'Yes, Do It!!!!',
           'Thank you for clicking me,\nYou are very cool Person']

TRIGGERSIZE = [30, 50]

BLACK = 0, 0, 0
SOME = 123, 12, 178
SOMEELSE = 30, 200, 96

SIZE = 500, 800

FONTNAME = 'comicsansms'
FONTSIZE = 25

MARGIN = 10


log = logging.getLogger()
h = logging.StreamHandler()
log.addHandler(h)
log.setLevel(logging.DEBUG)

log.info('Initialized Logger')


class View:
    def __init__(self, size):
        log.info('Pygame')
        pygame.init()
        log.info('Screen')
        self.screen = pygame.display.set_mode(size)

    def __call__(self):
        buttons = [get_button(BUTTONCOORDSONE, TXTSONE)]

        while True:
            for event in pygame.event.get():
                self.handle_event(event)

            # pr = False
            m = pygame.mouse

            for btn in buttons:
                btn.check()

                if m.get_pressed()[0] and m.get_pos() not in btn.trigger:
                    btn.trigger.resetcolswitch()

            self.screen.fill(BLACK)

            for btn in buttons:
                btn.draw(self.screen)

            pygame.display.flip()

            time.sleep(0.1)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


def get_button(cords, txts):
    trgr = RectTrigger(TRIGGERSIZE, SOME, SOMEELSE, cords)
    font = pygame.font.SysFont(FONTNAME, FONTSIZE)
    info = Information(font, cords, *TXTSONE)
    btn = Button(trgr, cords, info)
    return btn




if __name__ == '__main__':
    v = View(SIZE)
    v()
