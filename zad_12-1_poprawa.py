'''
EXERCISE 12.1
Write tests for the Vector class (Homework 6) using the 'unittest' or 'pytest' module.
'''

import math
import unittest

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

# Tests
class VectorTests(unittest.TestCase):
    def test_vector_equality(self):
        v = Vector(1, 2, 3)
        w = Vector(1, 2, 3)
        self.assertEqual(v, w)

    def test_vector_inequality(self):
        v = Vector(1, 2, 3)
        w = Vector(3, 2, 1)
        self.assertNotEqual(v, w)

    def test_vector_addition(self):
        v = Vector(1, 2, 3)
        w = Vector(3, 2, 1)
        result = v + w
        self.assertEqual(result, Vector(4, 4, 4))

    def test_vector_subtraction(self):
        v = Vector(1, 2, 3)
        w = Vector(3, 2, 1)
        result = v - w
        self.assertEqual(result, Vector(-2, 0, 2))

    def test_vector_multiplication(self):
        v = Vector(1, 2, 3)
        w = Vector(3, 2, 1)
        result = v * w
        self.assertEqual(result, 10)

    def test_vector_cross_product(self):
        v = Vector(1, 2, 3)
        w = Vector(3, 2, 1)
        result = v.cross(w)
        self.assertEqual(result, Vector(-4, 8, -4))

unittest.main()
