def divide_exact(n, d = 10):
    """
    Return the quotient and remainder of dividing N by D.
    >>> q, r = divide_exact(2013, 10);
    >>> q
    201
    >>> r
    3
    """
    return n // d, n % d;

quot, remn = divide_exact(2013, 10);