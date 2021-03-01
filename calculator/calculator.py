# _*_ encoding: utf-8 _*_

class Calculator(object):

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError('You can not divide a number by zero.')

        return x / y
