#
def greatest(name: str) -> str:
    return f"{name} is the Greatest!";
#

#
from operator import mul;
def square(nbr : int) -> int:
    return mul(nbr, nbr);
#

# out = greatest("Jesus");
out = square(-10);
# print(out);

### Pure Functions: just return values
signature = pow(2, 4);
print(signature);

### Non-Pure Functions: have side effects (return None)
print(print(1));