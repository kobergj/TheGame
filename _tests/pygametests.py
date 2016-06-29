import pygame
import time

import logging

size = [320, 240]
black = 0, 0, 0
white = 255, 255, 255
some = 123, 12, 178
someelse = 30, 200, 96

text = 'Please,\nClick me\nmy Friend!'
font = 'comicsansms'
fontsize = 25

log = logging.getLogger()
h = logging.StreamHandler()
log.addHandler(h)
log.setLevel(logging.WARNING)

log.info('Initialized Logger')

class View:
    def __init__(self):
        log.info('Pygame')
        pygame.init()
        log.info('Screen')
        self.screen = pygame.display.set_mode(size)
        log.info('Font')
        self.textfont = pygame.font.SysFont(font, fontsize)

    def __call__(self):
        bg = black
        col = some

        while True:
            for event in pygame.event.get():
                self.handle_event(event)

            bg, col, pr, trects = self.handle_loop(bg, self.textfont)

            self.handle_drawing(self.screen, bg, col, trects)

            if pr:
                time.sleep(0.1)


    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def handle_loop(self, bg, textfont):
        to_return = []

        pr = False
        m = pygame.mouse.get_pos()

        if 70 < m[0] < 130 and 70 < m[1] < 130:
            col = some
            if pygame.mouse.get_pressed()[0]:
                pr = True
                
                if bg == black:
                    bg = white
                else:
                    bg = black
        else:
            col = someelse

        txt_lines = text.split('\n')

        for txt in txt_lines:
            rendtext = textfont.render(txt, True, col)

            textrect = rendtext.get_rect()

            to_return.append([rendtext, textrect])

        return bg, col, pr, to_return

    def handle_drawing(self, screen, bg, col, txtrects):
        screen.fill(bg)

        i = 70
        for t in txtrects:
            t[1].topleft = [140, i]

            i += 25

            screen.blit(*t)

        pygame.draw.circle(screen, col, [100, 100], 30)

        pygame.display.flip()


if __name__ == '__main__':
    log.info('Init View')
    v = View()
    log.info('Start View')
    v()










