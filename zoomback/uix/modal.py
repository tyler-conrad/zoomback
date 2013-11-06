# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from os import listdir

from kivy.core.window import Window
from kivy.uix.modalview import ModalView
from kivy.uix.listview import ListView
from kivy.uix.togglebutton import ToggleButton
from kivy.adapters.listadapter import ListAdapter

from zoomback.util.query import kvquery as q
from zoomback.util.misc import root

class ListToggleButton(ToggleButton):
    def select(self, *args):
        self.state = 'down'
        next(q(Window, cls=['config_modal'])).dismiss()
        next(q(root(), cls=['selector'])).config = self.text

    def deselect(self, *args):
        self.state = 'normal'

class ConfigModal(ModalView):
    def __init__(self, **kw):
        kw['cls'] = ['config_modal']
        super(ConfigModal, self).__init__(**kw)
        def converter(row_index, obj):
            return {
                'text': obj,
                'size_hint_y': None,
                'height': 24}

        self.add_widget(
            ListView(adapter=ListAdapter(
                data=[
                    config.split('.')[0]
                    for config in listdir('zoomback/config/config')],
                args_converter=converter,
                selection_mode='single',
                propagate_selection_to_data=False,
                allow_empty_selection=True,
                cls=ListToggleButton)))
