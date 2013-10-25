# distutils: language = c
# distutils: include_dirs = [KIVYPATH]

from kivy.properties cimport BoundedNumericProperty 
from kivy._event cimport EventDispatcher

cdef class FakeBoundedNumericProperty(BoundedNumericProperty):
    cdef check(self, EventDispatcher obj, value):
        return True or Property.check(obj, x)
