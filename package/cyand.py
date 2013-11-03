from paver.easy import sh

from util import env
from util import change_ext

API = env('ANDROIDAPI')
NDKPATH = env('ANDROIDNDK')
P4APATH = env('P4APATH')
ABI = '4.8'

gcc     = ('{}/toolchains/arm-linux-androideabi-{}/prebuilt/linux-x86_64/'
    'bin/arm-linux-androideabi-gcc').format(NDKPATH, ABI)
sysroot = '{}/platforms/android-{}/arch-arm'.format(NDKPATH, API)
a_incl  = '-I' + sysroot + '/usr/include'
a_libs  = '-L' + sysroot + '/usr/lib'
p_incl  = '-I{}/build/python-install/include/python2.7'.format(P4APATH)
libs    = '-L{}/build/libs'.format(P4APATH)
p_libs  = '-L{}/build/python-install/lib'.format(P4APATH)


def cyand(c_path):
    o_path = change_ext(c_path, '.o')
    so_path = change_ext(o_path, '.so')

    obj_cmd = ('{} -mandroid -fomit-frame-pointer -DNDEBUG -g -O3 -Wall '
        '-Wstrict-prototypes -fPIC --sysroot {} {} {} -c {} -o {}').format(
            gcc,
            sysroot,
            a_incl,
            p_incl,
            c_path,
            o_path)
    print obj_cmd
    sh(obj_cmd)


    so_cmd = ('{} -shared -O3 -mandroid -fomit-frame-pointer --sysroot {} -lm '
        '-lGLESv2 -lpython2.7 {} {} {} {} -o {}').format(
            gcc,
            sysroot,
            libs,
            p_libs,
            a_libs,
            o_path,
            so_path)
    print so_cmd
    sh(so_cmd)