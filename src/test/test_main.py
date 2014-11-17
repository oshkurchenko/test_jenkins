import unittest
import main
from my_math import MyMath


class FirstPart(unittest.TestCase):

    def setUp(self):
        pass

    def test_first_method_13(self):
        foo = main.Foo()
        self.assertEqual(foo.first_method(), 13)

    def test_one_more_method_input_less_5(self):
        foo = main.Foo()
        self.assertEqual(foo.one_more_method(4), '444')

    def test_one_more_method_input_more_5(self):
        foo = main.Foo()
        self.assertEqual(foo.one_more_method(10), '1010')

    def test1(self):
        pass

    def test2(self):
        self.assertEqual(True, True)
    def test3(self):
        self.assertEqual(True, True)

    def test4(self):
        self.assertEqual(True, True)


class LastPart(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(True, True)

    def test2(self):
        self.assertEqual(True, True)

    def test3(self):
        self.assertEqual(True, True)

    def test4(self):
        self.assertEqual(True, True)

class MyMath_test(unittest.TestCase):
    def setUp(self):
        pass

    def test_sum(self):
        math = MyMath()
        self.assertEqual(math.sum(1,10,-3), 8)