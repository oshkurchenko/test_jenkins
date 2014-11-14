class Foo:
    def __init__(self):
        pass

    def first_method(self):
        a = 10
        return a + 3

    def one_more_method(self, a):
        b = str(a)*3
        if a > 5:
            b = str(a)*2
        return b