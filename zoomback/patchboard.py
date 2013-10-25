# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from kivy.uix.widget import Widget

from properties import FakeBoundedNumericProperty as FBNP
from slapdash import Walker

class PatchBoard(Widget):
    _x = FBNP(256, min=0, max=512)
    _y = FBNP(256, min=0, max=512)
    _w = FBNP(256, min=0, max=512)
    _h = FBNP(256, min=0, max=512)

class RandomProducer(PatchBoard):
    def __init__(self):
        self.walkers = [
            Walker(self, RandomProducer._x, min_dur=1.0, max_dur=5.0),
            Walker(self, RandomProducer._y, min_dur=1.0, max_dur=5.0)]
rp = RandomProducer()
