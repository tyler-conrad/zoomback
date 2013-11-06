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
        self.handle_select()

    def deselect(self, *args):
        self.state = 'normal'


class ConfigToggleButton(ListToggleButton):
    def handle_select(self):
        next(q(Window, cls=['config_modal'])).dismiss()
        next(q(root(), cls=['selector'])).config = self.text


class Modal(ModalView):
    def __init__(self, tag, load_dir, list_item_cls, **kw):
        kw['cls'] = [tag]
        super(Modal, self).__init__(**kw)

        def converter(row_index, obj):
            return {
                'text': obj,
                'size_hint_y': None,
                'height': 24}

        self.add_widget(
            ListView(adapter=ListAdapter(
                data=[
                    config.split('.')[0]
                    for config in listdir(load_dir)],
                args_converter=converter,
                selection_mode='single',
                propagate_selection_to_data=False,
                allow_empty_selection=True,
                cls=list_item_cls)))


class ConfigModal(Modal):
    def __init__(self, **kw):
        super(ConfigModal, self).__init__(
            tag='config_modal',
            load_dir='zoomback/config/config',
            list_item_cls=ConfigToggleButton, 
            **kw)
