# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from os import listdir

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty

from zoomback.uix.drawer.drawer import Drawer
from zoomback.util.misc import obj_name
from zoomback.util.query import kvquery as q
from zoomback.uix.drawer.nd import NavigationDrawerException

Builder.load_file('zoomback/uix/selector.kv')
class Selector(Drawer):
    config = StringProperty()
    filter = ObjectProperty()
    patch = StringProperty()

    def __init__(self, *args):
        super(Selector, self).__init__(*args)
        Clock.schedule_once(self.do_load, -1)

    def set_text(self, cls, text):
        next(q(self, cls=[cls])).text = text

    def do_load(self, dt):
        self.config = 'default'

    def on_config(self, src, config):
        self.set_text('config', config)

        try:
            self.remove_widget(self.main_panel)
        except AttributeError:
            pass
        config_widget = Builder.load_file(
            'zoomback/config/config/' + config + '.kv')
        self.add_widget(config_widget)

        self.filter_list = []
        for filter in config_widget.children:
            name = obj_name(filter)
            if name in ['Source', 'Sink']:
                continue
            self.filter_list.append(filter)
        self.filter = self.filter_list[0]

    def on_filter(self, src, filter):
        self.set_text('filter', obj_name(filter))

    def on_patch(self, src, patch):
        self.set_text('patch', patch)