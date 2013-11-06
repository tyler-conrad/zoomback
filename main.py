# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.widget import Widget

from zoomback.util.misc import root
from zoomback.patchloader import load
from zoomback.uix.selector import Selector

from zoomback.uix.frame import Frame

class ZoomBack(App):
    def build(self):
        r = root()
        if not r:
            r = Selector()
        return r

ZoomBack().run()
