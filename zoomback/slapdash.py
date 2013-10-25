# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""
from random import randrange
from random import choice

from kivy.animation import Animation

transition_list = [
    'in_back',
    'in_bounce',
    'in_circ',
    'in_cubic',
    'in_elastic',
    'in_expo',
    'in_out_back',
    'in_out_bounce',
    'in_out_circ',
    'in_out_cubic',
    'in_out_elastic',
    'in_out_expo',
    'in_out_quad',
    'in_out_quart',
    'in_out_quint',
    'in_out_sine',
    'in_quad',
    'in_quart',
    'in_quint',
    'in_sine',
    'linear',
    'out_back',
    'out_bounce',
    'out_circ',
    'out_cubic',
    'out_elastic',
    'out_expo',
    'out_quad',
    'out_quart',
    'out_quint',
    'out_sine']

class Walker(object):
    def __init__(
            self,
            widget,
            bnp,
            dur=None,
            trans=None,
            min_dur=None,
            max_dur=None):
        self.widget = widget
        self.bnp = bnp
        self.dur = dur
        self.trans = trans
        self.min_dur = min_dur
        self.max_dur = max_dur
        self.anim = self.build()

    def build(self):
        anim = Animation(
            duration=(
                self.dur
                if self.dur
                else randrange(self.min_dur, self.max_dur)),
            transition=(
                self.trans
                if self.trans
                else choice(transition_list)),
            **{self.bnp.name: randrange(
                self.bnp.get_min(self.widget),
                self.bnp.get_max(self.widget))})
        anim.bind(on_complete=self.on_complete)
        anim.start(self.widget)
        return anim

    def on_complete(self, anim, widget):
        self.anim = self.build()

class Stepper(object):
    pass

