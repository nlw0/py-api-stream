## Copyright 2013 Nicolau Leal Werneck
##
##    Licensed under the Apache License, Version 2.0 (the "License");
##    you may not use this file except in compliance with the License.
##    You may obtain a copy of the License at
##
##        http://www.apache.org/licenses/LICENSE-2.0
##
##    Unless required by applicable law or agreed to in writing, software
##    distributed under the License is distributed on an "AS IS" BASIS,
##    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##    See the License for the specific language governing permissions and
##    limitations under the License.

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
                    depends = ['PyTupleStream.h', 'PyTupleStream.cpp',
                               'ArrayManager.h', 'ArrayManager.cpp', ],
                    )

setup (name = 'TuStTest',
       version = '1.0',
       description = 'Test TupleStream class',
       ext_modules = [module1])
