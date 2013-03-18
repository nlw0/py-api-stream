import tusttest

def tfun1_proto(x,y):
    '''Python-prototype of test function 1.'''
    return x + y


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
    try:
        z = tusttest.tfun1(a)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'

    ## Test incorrect type
    try:
        z = tusttest.tfun1(d,a)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    try:
        z = tusttest.tfun1(d,d)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
    try:
        z = tusttest.tfun1(a,d)
    except TypeError as err:
        print 'OK, TypeError with message "' + err.message + '"'
