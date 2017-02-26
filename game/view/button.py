

class TextButton:
    def __init__(self, txt, colors, txtcordfunc):
        self._text = txt
        self._active = False
        self._color = colors
        self._validator = lambda x: True

        self.Coordinates = txtcordfunc
        # self.Color = self._color.UnClickable

    def Text(self):
        return self._text

    def Highlight(self, condargs, do=True):
        if not do:
            self.Color = self._colors.UnClickable
            return

        if self._validator(condargs):
            self.Color = self._colors.UnClickable
            return

        self.Color = self._colors.Clickable

    def Active(self):
        return self._active

    def DeActivate(self):
        self._active = False
    #    self.execfunc(execargs)


# class Validator:
#     def __init__(self, condfunc, execfunc, execargs):
#         self._conds = condfunc
#         self._func = (execfunc, execargs)

#     def __call__(self, condargs):
#         if self._conds(conda rgs):
#             return self._func

#         return
