# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from kivy.app import App

def obj_name(obj):
    return obj.__class__.__name__

def root():
    return App.get_running_app().root