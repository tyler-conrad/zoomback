# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from kivy.lang import Builder

from zoomback.patchboard import tpb
from zoomback.patchboard import pb

cur_patch = None
def load(patch):
    global cur_patch
    if cur_patch:
        Builder.unload_file(cur_patch)
    cur_patch = patch

    Builder.unbind_widget(pb.uid)
    Builder.load_file(patch)
    tpb.store()
    Builder.apply(pb)
    tpb.reset()
