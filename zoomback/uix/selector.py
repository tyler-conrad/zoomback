# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from os import listdir

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from zoomback.uix.drawer.drawer import Drawer

class Selector(Drawer):
    def __init__(self, *args):
        super(Selector, self).__init__(*args)
        
        side_panel = BoxLayout()
        for config_file in listdir('zoomback/config'):
            side_panel.add_widget(Button(text=config_file))
        self.add_widget(side_panel)