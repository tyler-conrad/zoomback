# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.widget import Widget

from zoomback.util import root
from zoomback.patchloader import load
from zoomback.uix.drawer.nd import NavigationDrawerException
from zoomback.uix.selector import Selector

class ZoomBack(App):
    def build(self, config='default'):
        r = root()
        if not r:
            r = Selector()

        try:
            r.remove_widget(r._main_panel)
        except NavigationDrawerException:
            pass

        r.add_widget(Builder.load_file('zoomback/config/' + config + '.kv'))
        return r

ZoomBack().run()
