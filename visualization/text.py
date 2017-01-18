

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
        colswitch = MouseStateSwitch(BLACK, SOME, BLACK)

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
