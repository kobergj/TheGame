import pygame
import time

import logging

SIZE = [640, 480]

BLACK = 0, 0, 0
WHITE = 255, 255, 255
SOME = 123, 12, 178
SOMEELSE = 30, 200, 96
COLTHREE = 92, 100, 12

TXTSONE = ['Please,\nClick me\nmy Friend!',
          'Yes, Do It!!!!',
          'Thank you for clicking me,\nYou are very cool Person']

TXTSTWO = ['Or me\nI also deserve it\nDude...',
          'I changed my mind,\nI dont wannabe \n clicked any more',
          'Oh, you clicked.\nOk...\nThanxs anyway.\nSee ya...']

FONTNAME = 'comicsansms'
FONTSIZE = 25

TRIGGERSIZE = 30

BUTTONCOORDSONE = 100, 400
BUTTONCOORDSTWO = 300, 100

MARGIN = 10

log = logging.getLogger()
h = logging.StreamHandler()
log.addHandler(h)
log.setLevel(logging.WARNING)

log.info('Initialized Logger')

# class View:
#     def __init__(self):
#         log.info('Pygame')
#         pygame.init()
#         log.info('Screen')
#         self.screen = pygame.display.set_mode(size)
#         log.info('Font')
#         self.textfont = pygame.font.SysFont(font, fontsize)

#     def __call__(self):
#         bg = black
#         col = some

#         while True:
#             for event in pygame.event.get():
#                 self.handle_event(event)

#             bg, col, pr, trects = self.handle_loop(bg, self.textfont)

#             self.handle_drawing(self.screen, bg, col, trects)

#             if pr:
#                 time.sleep(0.1)


#     def handle_event(self, event):
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     def handle_loop(self, bg, textfont):
#         to_return = []

#         pr = False
#         m = pygame.mouse.get_pos()

#         if 70 < m[0] < 130 and 70 < m[1] < 130:
#             col = some
#             if pygame.mouse.get_pressed()[0]:
#                 pr = True
                
#                 if bg == black:
#                     bg = white
#                 else:
#                     bg = black
#         else:
#             col = someelse

#         txt_lines = text.split('\n')

#         for txt in txt_lines:
#             rendtext = textfont.render(txt, True, col)

#             textrect = rendtext.get_rect()

#             to_return.append([rendtext, textrect])

#         return bg, col, pr, to_return

#     def handle_drawing(self, screen, bg, col, txtrects):
#         screen.fill(bg)

#         i = 70
#         for t in txtrects:
#             t[1].topleft = [140, i]

#             i += 25

#             screen.blit(*t)

#         pygame.draw.circle(screen, col, [100, 100], 30)

#         pygame.display.flip()

class View:
    def __init__(self, size):
        log.info('Pygame')
        pygame.init()
        log.info('Screen')
        self.screen = pygame.display.set_mode(size)

    def __call__(self):
        # bg = BLACK

        buttons = [get_button(BUTTONCOORDSONE, TXTSONE), get_button(BUTTONCOORDSTWO, TXTSTWO)]

        while True:
            for event in pygame.event.get():
                self.handle_event(event)

            # pr = False
            m = pygame.mouse

            for btn in buttons:
                btn.check()

                if m.get_pressed()[0] and m.get_pos() not in btn.trigger:
                    btn.trigger.resetcolswitch()

                # if bg == BLACK:
                #     bg = WHITE
                # else:
                #     bg = BLACK

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

    txtcrds = [cords[0] + TRIGGERSIZE + MARGIN, cords[1] - TRIGGERSIZE]

    trgr = CircleTrigger(TRIGGERSIZE, SOME, SOMEELSE, cords)

    btn = Button(trgr, cords)

    return btn

def get_text_button(cords, txts):
    font = pygame.font.SysFont(FONTNAME, FONTSIZE)

    info = Information(font, cords, *txts)

    trgr = RectTrigger([0, 0], SOME, SOMEELSE, [0, 0])

    btn = Button(trgr, cords, info)

    return btn


class ButtonContainer:
    def __init__(self, circlebutton, textbutton):
        self.circlebutton = circlebutton
        self.textbutton = textbutton

    def check(self):
        self.circlebutton.check()
        self.textbutton.check()


class Button:
    def __init__(self, trigger, cords, info=None):
        self.trigger = trigger

        self.info = info

        self.cords = cords

    def check(self):
        switch = MouseStateSwitch(lambda: None, self.trigger.activate, lambda: None)

        # relpos = [m[0]-c[0], m[1]-c[1]]
        # if relpos in self.trigger:
        #     self.trigger.activate()

        log.info('Switching Button evantually')
        switch(self.trigger)()

        if self.info:
            self.info.render(self.trigger)

    def draw(self, screen):

        self.trigger.draw(screen)

        if self.info:
            self.info.draw(screen)


class Trigger:
    def __init__(self, size, pass_col, act_col, coords):
        self.size = size

        # self._cols = [pass_col, act_col]
        self._colswitch = MouseStateSwitch(act_col, act_col, pass_col)
        self.active = False

        self._crds = coords

    def activate(self):
        self.active = True

    def color(self):
        return self._colswitch(self)

    def change_coordinates(self, cords):
        self._crds = cords

    def change_size(self, size):
        self.size = size

    def resetcolswitch(self):
        self._colswitch.deactivate()

class CircleTrigger(Trigger):
    def __contains__(self, item):
        s = self.size

        x = item[0] - self._crds[0]
        y = item[1] - self._crds[1]

        if -s < x < s and -s < y < s:
            return True

        return False

    def borders(self):
        s = self.size
        return [[-s,s], [-s,s]]

    def draw(self, screen):
        pygame.draw.circle(screen, self.color(), self._crds, self.size)

        if not pygame.mouse.get_pressed()[0]:
            self.active = False

class RectTrigger(Trigger):
    def __contains__(self, item):
        w = self._size[0]
        h = self._size[1]

        cx = self._crds[0]
        cy = self._crds[1]

        x = item[0]  # - cx
        y = item[1]  # - cy

        log.debug('Comparing %s to %s' % (item, [[cx, w], [cy, h]]))
        if cx <= x <= cx + w and cy <= y <= cy + h:
            return True

        return False

    def draw(self, screen, col):
        if col:
            log.debug('Drawing Rectangle with color %s' % [col])
            pygame.draw.rect(screen, col, (self._crds[0], self.crds[1], self.size[0], self.size[1]))



class Information:
    def __init__(self, font, coords, ptext, htext, ctext):
        self._fnt = font

        self._todraw = []

        self._switch = MouseStateSwitch(ctext, htext, ptext)

        self._crds = coords

    def render(self, trigger):
        txt = self._switch(trigger)

        txt_lines = txt.split('\n')

        i = self._crds[1]
        for t in txt_lines:
            line = TextLine(t, self._fnt, trigger.color(), [self._crds[0], i])

            i += FONTSIZE + MARGIN

            self._todraw.append(line)

    def draw(self, screen):
        colswitch = MouseStateSwitch(BLACK, COLTHREE, BLACK)

        for tl in self._todraw:
            col = colswitch(tl)

            tl.draw(screen, col)

        self._todraw = []

class TextLine:
    def __init__(self, txt, fnt, col, cords, highlight=False):
        self._text = fnt.render(txt, True, col)

        self._rect = self._text.get_rect()

        self._crds = cords

        self._hlght = highlight


    def draw(self, screen, col=None):
        self._rect.midleft = self._crds

        screen.blit(self._text, self._rect)


class MouseStateSwitch:
    def __init__(self, on_click=None, on_highlight=None, on_passive=None):
        self._mouse = pygame.mouse

        self.on_highlight = on_highlight
        self.on_click = on_click
        self.on_passive = on_passive

        self.active = False

    def __call__(self, container):
        # pos = self._mouse.get_pos()

        # log.debug('Comparing Position %s to container %s' % (pos, trigger.borders()))
        if self.active:
            return self.on_click
        
        if self._mouse.get_pos() in container:
            if self._mouse.get_pressed()[0]:
                self.active = True
                return self.on_click

            return self.on_highlight

        return self.on_passive

    def deactivate(self):
        self.active = False




if __name__ == '__main__':
    log.info('Init View')
    v = View(SIZE)
    log.info('Start View')
    v()










