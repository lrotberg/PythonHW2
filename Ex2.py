# Lior Rotberg - 201522372
# Chen Cohen - 305046385

import unittest


# ---------------------------------- Q1
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


# ---------------------------------- Q2
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Rational:
    _max = None
    max = _max

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Division by 0")
        else:
            self.n = numerator
            self.d = denominator
        if Rational._max is None or self > Rational._max:
            Rational._max = self
            Rational.max = "Rational(" + str(Rational._max) + ")"

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


# ---------------------------------- Q3
def my_zip(iterable1, iterable2, fill=None):
    iterable1 = iter(iterable1)
    iterable2 = iter(iterable2)
    for a in iterable1:
        # run on iterable1
        b = next(iterable2, fill)
        if b is None:
            return
        yield (a, b)

    b = next(iterable2, None)
    while b is not None:
        # b is longer than a
        if fill is None:
            return
        yield (fill, b)
        b = next(iterable2, None)


g = (3 * i for i in range(5))
for first, second in my_zip(g, ["a", "b", "c"], "bye"):
    print(first, second)


# ---------------------------------- Q5
def anagram(word):
    words = []
    matched = False
    file = open('words.txt', 'r')
    for line in file:
        if len(word) == len(line.strip()):
            for letter in word:
                matched = False
                if letter not in line:
                    matched = False
                    break
                else:
                    if word.count(letter) != line.strip().count(letter):
                        break
                    matched = True

            if matched:
                words.append(line.strip())

    file.close()
    return words


# ---------------------------------- tests
class TestRational(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Rational(5, 10)), '1/2')
        self.assertEqual(str(Rational(8, 24)), '1/3')

    def test_repr(self):
        self.assertEqual(repr(Rational(5, 10)), 'Rational(1, 2)')
        self.assertEqual(repr(Rational(8, 24)), 'Rational(1, 3)')

    def test_gt(self):
        self.assertGreater(Rational(5, 10), Rational(8, 24))

    def test_lt(self):
        self.assertLess(Rational(8, 24), Rational(5, 10))

    def test_max(self):
        half = Rational(1, 2)
        self.assertEqual(Rational.max, 'Rational(1/2)')
        two = Rational(2, 1)
        self.assertEqual(Rational.max, 'Rational(2/1)')
        self.assertNotEqual(Rational.max, 'Rational(1/2)')


class TestAnagram(unittest.TestCase):

    def test_anagram(self):
        self.assertEqual(anagram('restful'), ['fluster', 'fluters', 'restful'])
        self.assertEqual(anagram('lore'), ['lore', 'orle', 'role'])
        self.assertEqual(anagram(''), [])


# ---------------------------------- main
if __name__ == '__main__':
    # print(sum2(1, 2))
    # print(sum2(2, 4))
    # print(sum2(1, 2))
    unittest.main()


# half = Rational(5, 10)
# print(str(half))
# print(repr(half))
# print(Rational.max)
# third = Rational(8, 24)
# print(str(third))
# print(half+third)
# print(third-half)
# print(half*third)
# print(half/third)
# print(half == third)
# print(half != third)
# print(half < third)
# print(half <= third)
# print(half > third)
# print(half >= third)
# print(Rational.max)
# two = Rational(2)
# print(repr(two))
# print(half)
# print(repr(Rational.self.max))
