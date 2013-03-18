import tusttest

def tfun1_proto(a,b):
    '''Python-prototype of test function 1.'''
    return a + b

def tfun2_proto(a, b):
    '''Python-prototype of test function 2.'''
    return a * b


if __name__ == '__main__':
    a = 1
    b = 2
    c = 3

    d = 1.0

    print 'a:', a
    print 'b:', b
    z = tusttest.tfun1(a, b)
    print 'z=', z

    assert z == tfun1_proto(a,b)
        

    ## Test insufficient number of args
    try:
        z = tusttest.tfun1()
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun1(a)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    else:
        raise Exception('FAIL No exception was risen.')

    ## Test incorrect type
    try:
        z = tusttest.tfun1(d,a)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun1(d,d)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun1(a,d)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    else:
        raise Exception('FAIL No exception was risen.')


    a = 11
    b = 3

    d = 3.14

    print 'a:', a
    print 'd:', d
    z = tusttest.tfun2(a, d)
    print 'z=', z

    assert z == tfun2_proto(a, d)


    ## Test insufficient number of args
    try:
        z = tusttest.tfun2()
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun2(a)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun2(d)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    else:
        raise Exception('FAIL No exception was risen.')

    ## Test incorrect type
    try:
        z = tusttest.tfun2(d,a)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    else:
        raise Exception('FAIL No exception was risen.')
    try:
        z = tusttest.tfun2(d,d)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    else:
        raise Exception('FAIL No exception was risen.')

    ## Check that int -> double converison works.
    z = tusttest.tfun2(a,b)
    if z == tfun2_proto(a,b):
        print "OK int -> float conversion."
    else:
        raise Exception('FAIL int -> float conversion.')
