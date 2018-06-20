## Copyright 2013-2018 Nicolau Leal Werneck
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

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


# https://stackoverflow.com/a/49041815/160466
# Avoid a gcc warning below:
# cc1plus: warning: command line option ‘-Wstrict-prototypes’ is valid for C/ObjC but not for C++
class BuildExt(build_ext):
    def build_extensions(self):
        self.compiler.compiler_so.remove('-Wstrict-prototypes')
        super(BuildExt, self).build_extensions()


module1 = Extension(
    'tusttest',
    sources=['tusttest_module.cpp'],
    depends=[
        'PyTupleStream.h', 'PyTupleStream.cpp',
        'ArrayManager.h', 'ArrayManager.cpp',
    ],
)

setup(
    name='TuStTest',
    version='1.0',
    description='Test TupleStream class',
    ext_modules=[module1],
    cmdclass={'build_ext': BuildExt},
)
