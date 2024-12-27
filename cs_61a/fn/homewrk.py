#
def a_plus_abs_b (a: int, b: int) -> int:
    if (b >= 0): return a + b
    return a + (-b);
#

#
def two_of_three (i: int, j: int, k: int) -> int:
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    maxTmp = max(i, j, k);
    if (maxTmp == i):
        return j*j + k*k;
    elif (maxTmp == j):
        return i*i + k*k;
    else:
        return i*i + j*j;
#   
    
#
def largest_factor (n: int) -> int:
    """
    Return the largest factor of n that is smaller than n.
    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    nTmp = n - 1;
    while nTmp > 0:
        if (n % nTmp == 0): return nTmp;
        nTmp -= 1;
    return 1;
#

#
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    length = 1;
    while (n != 1):
        if (n % 2 == 0):
            n = n // 2
        else:
            n = (n * 3) + 1
        print(n);
        length += 1;
    return length;
#

# Execution Time
# print(a_plus_abs_b(2, -3));
# print(two_of_three(10, 2, 8));
# print(largest_factor(13));
# a = hailstone(27)
# print('a:', a)