# Copyright (c) Tyler Conrad.
# See LICENSE for details.

"""

"""
from sys import exit
from setuptools import find_packages
from os import environ

from paver.setuputils import setup
from paver.options import Bunch
from paver.path import path
from paver.tasks import task
from paver.tasks import needs
from paver.easy import error
from paver.easy import no_help
from Cython.Build.Dependencies import cythonize

import distutils.command.build_ext
import Cython.Distutils.build_ext
distutils.command.build_ext = Cython.Distutils.build_ext

try:
    KIVYPATH = path(environ['KIVYPATH'])
except KeyError:
    error('KIVYPATH environment variable not set.')
    exit(1)

def find(glob, dir=path('zoomback')):
    return dir.walkfiles(glob)

setup(**Bunch(
    name='ZoomBack',
    description='Visual feedback generator.',
    long_description='',
    url='',
    download_url='',
    version='0.0.1',
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
    package_dir={'.': 'zoomback'},
    packages=find_packages('.'),
    package_data={'zoomback': ['view/*.kv']},
    install_requires=["kivy"],
    tests_require=[],
    classifiers=[]
))

def change_ext(file, ext):
    return file.parent / file.namebase + ext

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
def clean_package():
    for c in find('*.c'):
        c.remove()
    for so in find('*.so'):
        so.remove()

@task
@needs('py_from_pyx', 'clean_package')
def uncomp():
    pass

@task
def del_pyc():
    for pyc in find('*.pyc'):
        pyc.remove()

@task
def clean():
    path("build").rmtree_p()
