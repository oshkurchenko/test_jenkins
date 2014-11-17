class MyMath:

    def sum(self, args):
        sum = 0
        for arg in args:
            sum += arg
        return sum

    def multiply(self, args):
        if 0 in args:
            return 0
        mult = 1
        for arg in args:
            mult *= arg
        return mult

class ToString:

    def convert_to_sring(self, a):
        return str(a)
