class MyMath:
    """
    Doc
    """
    def sum(self, args):
        """
        Doc
        :param args:
        :return:
        """
        sum = 0
        for arg in args:
            sum += arg
        return sum

    def multiply(self, args):
        """
        Doc
        :param args:
        :return:
        """
        if 0 in args:
            return 0
        mult = 1
        for arg in args:
            mult *= arg
        return mult

class ToString:
    """
    Doc
    """

    def convert_to_sring(self, a):
        """
        doc
        :param a:
        :return:
        """
        return str(a)
