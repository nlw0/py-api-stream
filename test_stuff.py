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

import tusttest
import numpy


def tfun1_proto(a, b):
    '''Python-prototype of test function 1.'''
    return a + b


def tfun2_proto(a, b):
    '''Python-prototype of test function 2.'''
    return a * b


def tfun3_proto(a, b):
    '''Python-prototype of test function 2.'''
    return a * (b[0, 0] * b[1, 1] - b[1, 0] * b[0, 1])


if __name__ == '__main__':
    ## Test first prototype function
    a = 1
    b = 2
    c = 3

    d = 1.0

    print('a:', a)
    print('b:', b)
    z = tusttest.tfun1(a, b)
    print('z=', z)

    assert z == tfun1_proto(a, b)

    ## Test insufficient number of args
    try:
        z = tusttest.tfun1()
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun1(a)
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')

    ## Test incorrect type
    try:
        z = tusttest.tfun1(d, a)
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun1(d, d)
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun1(a, d)
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')

    ## Test second prototype function
    a = 11
    b = 3

    d = 3.14

    print('a:', a)
    print('d:', d)
    z = tusttest.tfun2(a, d)
    print('z=', z)

    assert z == tfun2_proto(a, d)

    ## Test insufficient number of args
    try:
        z = tusttest.tfun2()
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun2(a)
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun2(d)
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')

    ## Test incorrect type
    try:
        z = tusttest.tfun2(d, a)
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun2(d, d)
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')

    ## Check that int -> double converison works.
    z = tusttest.tfun2(a, b)
    if z == tfun2_proto(a, b):
        print("OK int -> float conversion.")
    else:
        raise Exception('FAIL int -> float conversion.')

    ## Test third prototype function
    a = 3.0
    b = numpy.array([[1.0, 2.0], [3.0, 4.0]], dtype=numpy.double)
    b1 = numpy.array([1.0, 2.0, 3.0, 4.0])
    b3 = numpy.ones((3, 3, 3))
    z = tusttest.tfun3(a, b)
    assert z == tfun3_proto(a, b)

    try:
        z = tusttest.tfun3(a, b1)
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')

    try:
        z = tusttest.tfun3(a, b3)
    except TypeError as err:
        print('OK, TypeError with message "' + str(err) + '"')
    else:
        raise Exception('FAIL No exception was risen.')
