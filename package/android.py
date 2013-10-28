# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""

from os import environ

from paver.easy import sh
from paver.path import path

from package.util import env
from package.util import QueryDict

class Config(object):
    def __init__(self):
        opt = self.options = QueryDict()
        opt.name = 'zoomback'
        opt.package = '.'.join(['com', 'dodeca', opt.name])
        opt.version = sh('git describe --tags master', capture=True).split('-')[0]
        opt.dir = path('zoomback').realpath()
        opt.private = None
        opt.launcher = None
        opt.icon_name = None
        opt.orientation = 'sensor'
        opt.permission = None
        opt.ignore_path = None
        opt.icon = None
        opt.presplash = None
        opt.install_location = 'auto'
        opt.compile_pyo = None
        opt.intent_filters = None
        opt.blacklist = path('package').realpath() / 'blacklist.txt'
        opt.sdk = '8'
        opt.minsdk = '8'
        opt.window = None

    def option_string(self):
        return ' '.join([
            '--' + key.replace('_', '-') + ' ' + val
            for key, val in self.options.iteritems()
            if val is not None])
