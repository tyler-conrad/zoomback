# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from functools import partial

from kivy.clock import Clock
from kivy.uix.widget import Widget

from properties import FakeBoundedNumericProperty as FBNP
from slapdash import Walker

class PatchBoard(Widget):
    _x = FBNP(256, min=0, max=512)
    _y = FBNP(256, min=0, max=512)

TWEEN_DUR = 4.0
TWEEN_STEP = 1.0 / 60.0
class TweenerPatchBoard(PatchBoard):
    def __init__(self, pb, **kw):
        super(TweenerPatchBoard, self).__init__(**kw)
        self.pb = pb
        self.callbacks = {}

    def prop_names(self):
        cls = self.pb.__class__
        return [
            attr_name
            for attr_name in dir(cls)
            if isinstance(getattr(cls, attr_name), (FBNP,))]

    def disconnect(self):
        for prop_name in self.prop_names():
            try:
                self.pb.unbind(**{prop_name: self.callbacks[prop_name]})
            except KeyError:
                pass

    def store(self):
        self.disconnect()
        for prop_name in self.prop_names():
            setattr(self, prop_name, getattr(self.pb, prop_name))

    def reset(self):
        self.progress = 0.0
        Clock.unschedule(self.on_timer)
        Clock.schedule_interval(self.on_timer, TWEEN_STEP)

    def on_timer(self, dt):
        if self.progress > 1.0:
            Clock.unschedule(self.on_timer)
            for prop_name in self.prop_names():
                cb = self.callbacks[prop_name] = self.setter(prop_name)
                self.pb.bind(**{prop_name: cb})
            return

        for prop_name in self.prop_names():
            cur_val = getattr(self, prop_name)
            setattr(self, prop_name, cur_val 
                + (getattr(self.pb, prop_name) - cur_val)
                * self.progress)
            self.progress += (dt / TWEEN_DUR)

class RandomProducer(PatchBoard):
    def __init__(self, **kw):
        super(RandomProducer, self).__init__(**kw)
        self.walkers = {
            RandomProducer._x.name:
                Walker(self, RandomProducer._x, min_dur=1.0, max_dur=5.0),
            RandomProducer._y.name:
                Walker(self, RandomProducer._y, min_dur=1.0, max_dur=5.0)}

pb = PatchBoard()
tpb = TweenerPatchBoard(pb)
rp = RandomProducer()
