import unittest


class FirstPart(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        pass
    def test2(self):
        self.assertEqual(True, True)


class LastPart(unittest.TestCase):
    def setUp(self):
        pass
    
    def test1(self):
        self.assertEqual(False, True)

    def test2(self):
        self.assertEqual(True, False)

    def test3(self):
        self.assertEqual(True, False)