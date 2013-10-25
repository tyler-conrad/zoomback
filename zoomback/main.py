# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

from kivy.clock import Clock

from patchloader import load

class Test(Widget):
    _x = NumericProperty()
    _y = NumericProperty()

class ZoomBack(App):
    def load_blank(self, dt):
        load('zoomback/blank.kv')
    
    def load_blah(self, dt):
        load('zoomback/patch.kv')
    
    def build(self):
        load('zoomback/patch.kv')
        Clock.schedule_once(self.load_blank, 5)
        Clock.schedule_once(self.load_blah, 10)
        return Builder.load_string('''
#:import pb board.pb

Test:
    _x: pb._x
    _y: pb._y
    canvas:
        Color:
            rgb: 1.0, 1.0, 1.0
        Point:
            points: [self._x, self._y]
''')
ZoomBack().run()
