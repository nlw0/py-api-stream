from distutils.core import setup, Extension

## Remove -Wstrict-prototypes from compiler args.
## http://stackoverflow.com/questions/8106258/cc1plus-warning-command-line-option-wstrict-prototypes-is-valid-for-ada-c-o
import os
from distutils.sysconfig import get_config_vars

(opt,) = get_config_vars('OPT')
os.environ['OPT'] = " ".join(
    flag for flag in opt.split() if flag != '-Wstrict-prototypes'
)
## ===

module1 = Extension('tusttest',
                    sources = ['tusttest_module.cpp'],
                    depends = ['PyTupleStream.cpp'])

setup (name = 'TuStTest',
       version = '1.0',
       description = 'Test TupleStream class',
       ext_modules = [module1])
