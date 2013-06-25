import unittest
from vec2d import Vec2D


class Vec2D_test(unittest.TestCase):
    def setUp(self):
        self.a = Vec2D(42, 26)
        self.b = Vec2D(23, -12)

    def test_eq(self):
        self.assertEqual(self.a, self.a)
        self.assertEqual(Vec2D(2, 3), Vec2D(2, 3))
        self.assertNotEqual(Vec2D(2, 3), Vec2D(3, 2))

    def test_add(self):
        result = self.a + self.b
        self.assertEqual(result, Vec2D(42 + 23, 26 - 12))

    def test_mult(self):
        result = self.a * 2
        self.assertEqual(result, Vec2D(84, 52))

    def test_neg(self):
        self.assertEqual(-self.a, Vec2D(-42, -26))

    def test_iter(self):
        self.assertEqual(list(self.a), [42, 26])