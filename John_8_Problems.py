from math import pi





def a(a, b):
    multiple = a * b
    if multiple > 1000:
        return a + b
    else:
        return multiple

def b(a, b, c):
    if a % 5 == int():
        print a, 'is divisable by 5.'
    if b % 5 == int():
        print b, 'is divisable by 5.'
    if c % 5 == int():
        print c, 'is divisable by 5.'
#    else:
#        print 'None of these are divisible by 5.'

def c(r):
    area = (r ** 2) * pi
    return area

def d():
    first = raw_input('Please give your first name:')
    last = raw_input('Please give your last name:')
    print 'Hello', last, ',', first #fix so there is no space between comma!

''' def e(n):
    str(n)
    m = 'n' + 'n'
    b = 'n' + 'n' + 'n'
    add = int(n) + int(m) + int(b)
    return add
'''
def f(n):
    if n < 17:
        sub = 17 - n
        if sub >= 17:
            return 2 * sub
    if n >= 17:
        sub = n - 17
        if sub >= 17:
            return 2 * sub
    else:
        return sub





