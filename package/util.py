# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from os import environ

from paver.easy import sh
from paver.easy import path
from paver.easy import error

def version():
    return sh('git describe --tags master', capture=True).split('-')[0]

def env(env_var):
    try:
        return path(environ[env_var])
    except KeyError:
        error(env_var + ' environment variable not set.')
        exit(1)

def change_ext(file, ext):
    return file.parent / file.namebase + ext

class QueryDict(dict):
    def __getattr__(self, attr):
        try:
            return self.__getitem__(attr)
        except KeyError:
            return super(QueryDict, self).__getattr__(attr)

    def __setattr__(self, attr, value):
        self.__setitem__(attr, value)
