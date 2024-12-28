"""
    An environment is a sequence of frames
    1. The global frame alone
    2. A local frame
"""

from operator import mul, add;
#
def square(x):
    return mul(x, x);
square(square(3));
#
# print(add( add(2, mul(3, 4)), 5 ));
#

# DIVISION
from operator import truediv, floordiv, mod;
# True Division
print(2013 / 10);
print(truediv(2013, 10));
# Integer Division
print(2013 // 10);
print(floordiv(2013, 10));
# Exact Division
quotient = 2013 // 10;      # 201
remainder = 2013 % 10;       # 3
remainder = mod(2013, 10);   # 3
print(quotient);
print(remainder);