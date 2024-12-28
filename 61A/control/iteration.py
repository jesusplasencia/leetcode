def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    i = 1;
    while (i <= n):
        if (i % 3 == 0 and i % 5 == 0):
            print('fizzbuzz');
        elif (i % 3 == 0):
            print('fizz');
        elif (i % 5 == 0):
            print('buzz');
        else:
            print(i)
        i += 1;
        
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    iterator = 1;
    count_divisibles = 0;
    while (iterator <= n):
        if (n % iterator == 0):
            count_divisibles += 1;
        iterator += 1;
    return count_divisibles == 2;

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    iterator = 0;
    counter = 0;
    while (iterator <= 9):
        if has_digit(n, iterator):
            counter += 1;
        iterator += 1;
    return counter;
    
def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    nTmp = str(n);
    kTmp = str(k);
    return kTmp in nTmp;