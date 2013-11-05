# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""
from kivy.uix.layout import Layout
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

class Frame(Layout):
    def __init__(self, **kw):
        super(Frame, self).__init__(**kw)
        self.bind(
           children=self._trigger_layout,
           parent=self._trigger_layout,
           size=self._trigger_layout,
           pos=self._trigger_layout)
    
    def do_layout(self, *largs):
        for child in self.children:
            child.pos = self.pos
            child.size = self.size
