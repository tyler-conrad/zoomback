# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""
from sys import exit
from setuptools import find_packages
from os import environ

from paver.setuputils import setup
from paver.easy import Bunch
from paver.easy import path
from paver.easy import sh
from paver.easy import task
from paver.easy import needs
from paver.easy import no_help
from paver.easy import consume_args
from paver.easy import debug
from paver.easy import error
from Cython.Build.Dependencies import cythonize

import distutils.command.build_ext
import Cython.Distutils.build_ext
distutils.command.build_ext = Cython.Distutils.build_ext

from package.util import version
from package.util import env
from package.util import change_ext
from package.android import Config
from package.cyand import cyand

KIVYPATH = env('KIVYPATH')
P4APATH = env('P4APATH')

def find(glob, dir=path('zoomback')):
    return dir.walkfiles(glob)

setup(**Bunch(
    name='ZoomBack',
    description='Visual feedback generator.',
    long_description='',
    url='',
    download_url='',
    version=version(),
    license='',
    author='Tyler Conrad',
    author_email='conradt80@gmail.com',
    maintainer='',
    maintainer_email='',
    scripts=[],
    ext_modules=cythonize(
        module_list=map(str, find('*.pyx')),
        include_path=['.', KIVYPATH],
        aliases={
            'KIVYPATH': KIVYPATH}),
    packages=['zoomback'],
    package_data={'zoomback': ['*.kv']},
    install_requires=['kivy'],
    tests_require=[],
    classifiers=[]))

@task
@no_help
def pyx_from_py():
    renamed = []
    for py_mod in find('*.py'):
        if py_mod.namebase in ['main']:
            continue
        as_pyx = change_ext(py_mod, '.pyx')
        py_mod.rename(as_pyx)
        renamed += [as_pyx]
    if renamed:
        with open('.renamed', 'w+') as log:
            log.write('\n'.join(renamed))

@task
@needs(['pyx_from_py', 'build_ext'])
def comp():
    pass

@task
def py_from_pyx():
    try:
        with open('.renamed', 'r') as log:
            renamed = log.read().split()
    except IOError as ioe:
        error(ioe)
        return

    for pyx_file in renamed:
        file = path(pyx_file)
        try:
            file.rename(change_ext(file, '.py'))
        except OSError as ioe:
            error(ioe)
            continue

@task
@needs('py_from_pyx', 'clobber')
def uncomp():
    pass

def remove(glob):
    for match in find(glob):
        match.remove()

@task
def del_pyc():
    remove('*.pyc')

@task
def del_pyo():
    remove('*.pyo')

@task
def del_c():
    remove('*.c')

@task
def del_o():
    remove('*.o')

@task
def del_so():
    remove('*.so')

@task
def clean():
    path("build").rmtree_p()

@task
@needs(['clean','del_pyc', 'del_pyo', 'del_c', 'del_o', 'del_so'])
def clobber():
    pass

@task
@consume_args
def p4a_dist(args):
    mod_list = ['kivy']
    dist_name = args[0] if args else None
    clean_flag = '-f' if 'clean' in args else ''
    sh((P4APATH / 'distribute.sh')
        + ((' -d ' + dist_name) if dist_name else '')
        + ' -m "' + ' '.join(mod_list) + '"'
        + ' ' + clean_flag,
        cwd=P4APATH)
    dist_root = P4APATH / 'dist' / dist_name 
    (dist_root / 'default.properties').rename(dist_root / 'project.properties')

@task
@consume_args
def p4a_build(args):
    for c_file in find('*.c'):
        cyand(c_file)
    
    dist_path = P4APATH / 'dist' / args[0]
    sh((dist_path / 'build.py') + ' '
        + Config().option_string() + ' '
        + args[1],
        cwd=dist_path)
