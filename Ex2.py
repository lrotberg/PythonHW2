def memoize(func):
    cache = {}

    def closure(*args):
        if args not in cache:
            value = func(*args)
            cache[args] = value
        else:
            value = cache[args]
        return value

    return closure


@memoize
def sum2(x, y):
    print('calling sum2')
    return x + y


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Rational:
    max = None

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Division by 0")
        else:
            self.n = numerator
            self.d = denominator
        if Rational.max is None or self > Rational.max:
            Rational.max = self

    def __get__(self, instance, owner):
        return self

    def __add__(self, other):
        return Rational(self.n * other.d + other.n * self.d,
                        self.d * other.d)

    def __sub__(self, other):
        return Rational(self.n * other.d - other.n * self.d,
                        self.d * other.d)

    def __mul__(self, other):
        return Rational(self.n * other.n, self.d * other.d)

    def __truediv__(self, other):
        return Rational(self.n * other.d, self.d * other.n)

    def __lt__(self, other):
        return self.n * other.d < self.d * other.n

    def __le__(self, other):
        return not other < self

    def __eq__(self, other):
        return (self.n == other.n) and (self.d == other.d)

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return not other > self

    def __str__(self):
        g = gcd(self.n, self.d)
        n = self.n // g
        d = self.d // g
        return "%d/%d" % (n, d)

    def __repr__(self):
        g = gcd(self.n, self.d)
        n = self.n // g
        d = self.d // g
        return "Rational(%d, %d)" % (n, d)


print(Rational.max)
half = Rational(5, 10)
print(Rational.max)
two = Rational(2, 1)
print(half.max)
print(Rational.max)
# print(half)
# print(repr(Rational.self.max))
