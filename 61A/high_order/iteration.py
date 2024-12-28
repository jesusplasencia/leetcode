def fib(n):
    assert n >= 0, 'the input must be greater or equal to 0'
    pred, curr = 1, 0;
    k = 0;
    while k < n:
        pred, curr = curr, pred + curr;
        k = k + 1;
    return curr;

def if_(c, t, f):
    if c:
        return t;
    else:
        return f;
    
from math import sqrt;
def real_sqrt (x):
    """Return the real part of the square root of x"""
    if (x >= 0):
        return sqrt(x);
    else:
        return 0;

def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10;