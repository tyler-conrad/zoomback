# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.widget import Widget
 
from zoomback.patchloader import load
 
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
#:import tpb zoomback.patchboard.tpb
  
Widget:
    canvas:
        Color:
            rgb: 1.0, 1.0, 1.0
        Point:
            points: [tpb._x, tpb._y]
''')
ZoomBack().run()
