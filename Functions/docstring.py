# allows to comment inside a function

def test(a):
    '''
    Info: this function tests and prints parameter a
    '''
    print(a)

print(test.__doc__)