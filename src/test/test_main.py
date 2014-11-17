import unittest
import main


class FirstPart(unittest.TestCase):

    def setUp(self):
        pass

    def test_first_method_13(self):
        self.assertEqual(main.first_method(), 13)

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