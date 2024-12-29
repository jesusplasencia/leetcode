def apply_twice(f, x):
    return f(f(x));

def square(x):
    return x * x;

def make_adder(n):
    def adder(k):
        return k + n;
    return adder;

def f(x, y):
    return g(x, y);

def g(a, y):
    return a + y;